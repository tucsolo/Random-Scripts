#!/bin/bash
#https://medium.com/@kiranps11/kafka-and-zookeeper-multinode-cluster-setup-3511aef4a505
KAFKAURL="https://downloads.apache.org/kafka/2.6.0/kafka_2.13-2.6.0.tgz"
MYID=$1
MYID2=$(( MYID - 1 ))
echo "disabling selinux"
setenforce 0
echo "$MYID $MYID2"
echo "creating directory"
cd /
mkdir kafka
cd kafka
echo "downloading kafka"
curl -k $KAFKAURL > kafka.tgz
echo "decompressing kafka"
tar -xf kafka.tgz
rm -rf kafka.tgz
mv kafka* kafka
cp -dpRv kafka/* .
rm -rf kafka/
echo "configuring zookeeper"
mkdir -p data/zookeeper
mkdir -p config
echo $MYID > data/zookeeper/myid
cat <<EOF > config/zookeeper.properties
dataDir=/kafka/data/zookeeper
clientPort=2181
a non-production config
tickTime=2000
initLimit=5
syncLimit=2
server.1=192.168.240.21:2666:3666
server.2=192.168.240.22:2666:3666
server.3=192.168.240.23:2666:3666
zookeeper.connect=192.168.240.21:2181,192.168.240.22:2181,192.168.240.23:2181
maxClientCnxns=0
EOF
echo "configuring broker"
cat <<EOF > config/server.properties
broker.id=$MYID
num.network.threads=3
num.io.threads=8
socket.send.buffer.bytes=102400
socket.receive.buffer.bytes=102400
socket.request.max.bytes=104857600
log.dirs=/tmp/kafka-logs
num.partitions=1
num.recovery.threads.per.data.dir=1
offsets.topic.replication.factor=1
transaction.state.log.replication.factor=1
transaction.state.log.min.isr=1
log.retention.hours=168
log.segment.bytes=1073741824
log.retention.check.interval.ms=300000
zookeeper.connection.timeout.ms=18000
group.initial.rebalance.delay.ms=0
port=9093
zookeeper.connect=192.168.240.21:2181,192.168.240.22:2181,192.168.240.23:2181
EOF
#advertised.host.name = localhost
