//pins
int v24a = 2;
int v24b = 3;
int v24c = 4;
int v24s = 5;
int v5a = 8;
int v5b = 9;
int v5c = 10;
int v5d = 11;
int i;
void setup() {
  pinMode(v24a, OUTPUT);
  pinMode(v24b, OUTPUT);
  pinMode(v24c, OUTPUT);
  pinMode(v24s, OUTPUT);
  pinMode(v5a, OUTPUT);
  pinMode(v5b, OUTPUT);
  pinMode(v5c, OUTPUT);
  pinMode(v5d, OUTPUT);
}

void loop()
{
  poff();

  p24a();
  p5loop(200);
  p24b();
  p5loop(200);
  p24c();
  p5loop(200);
  p24d();
  p5loop(200);
  digitalWrite(v24s, HIGH);
  p24a();
  p5loop(200);
  p24b();
  p5loop(200);
  p24c();
  p5loop(200);
  p24d();
  p5loop(200);

}

void poff()
{
  digitalWrite(v24a, LOW);
  digitalWrite(v24b, LOW);
  digitalWrite(v24c, LOW);
  digitalWrite(v24s, LOW);
  digitalWrite(v5a, LOW);
  digitalWrite(v5b, LOW);
  digitalWrite(v5c, LOW);
  digitalWrite(v5d, LOW);
}

void p24a()
{
  digitalWrite(v24a, LOW);
  digitalWrite(v24b, LOW);
  digitalWrite(v24c, LOW);
}
void p24b()
{
  digitalWrite(v24a, LOW);
  digitalWrite(v24b, LOW);
  digitalWrite(v24c, HIGH);
}
void p24c()
{
  digitalWrite(v24a, HIGH);
  digitalWrite(v24b, LOW);
  digitalWrite(v24c, LOW);
}
void p24d()
{
  digitalWrite(v24a, HIGH);
  digitalWrite(v24b, HIGH);
  digitalWrite(v24c, LOW);
}
void p5a()
{
  digitalWrite(v5a, HIGH);
  digitalWrite(v5b, LOW);
  digitalWrite(v5c, LOW);
  digitalWrite(v5d, LOW);
}

void p5b()
{
  digitalWrite(v5a, LOW);
  digitalWrite(v5b, HIGH);
  digitalWrite(v5c, LOW);
  digitalWrite(v5d, LOW);
}
void p5c()
{
  digitalWrite(v5a, LOW);
  digitalWrite(v5b, LOW);
  digitalWrite(v5c, HIGH);
  digitalWrite(v5d, LOW);
}
void p5d()
{
  digitalWrite(v5a, LOW);
  digitalWrite(v5b, LOW);
  digitalWrite(v5c, LOW);
  digitalWrite(v5d, HIGH);
}
void p5loop(int dtime)
{
  p5a();
  delay(dtime);
  p5b();
  delay(dtime);
  p5c();
  delay(dtime);
  p5d();
  delay(dtime);
}
