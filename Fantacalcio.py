#!/usr/bin/env python 
import sys
import os
import csv

def main(args):
	p17 = []
	d17 = []
	c17 = []
	a17 = []
	p18 = []
	d18 = []
	c18 = []
	a18 = []
	op = []
	od = []
	oc = []
	oa = []
	
	with open('2017.csv', 'rb') as csv2017:
		data2017 = csv.reader(csv2017, delimiter=',', quotechar=';')
		for row in data2017:
			#print row
			if row[1] == 'P':
				p17.append(row)
			if row[1] == 'D':
				d17.append(row)
			if row[1] == 'C':
				c17.append(row)
			if row[1] == 'A':
				a17.append(row)

	with open('2018.csv', 'rb') as csv2018:
		data2018 = csv.reader(csv2018, delimiter=',', quotechar=';')
		for row in data2018:
			#print row
			if row[1] == 'P':
				p18.append(row)
			if row[1] == 'D':
				d18.append(row)
			if row[1] == 'C':
				c18.append(row)
			if row[1] == 'A':
				a18.append(row)
	while p18:
		g = []
		a = p18.pop()
		g.append(a[2])					#Nome
		g.append(a[3])					#Squadra attuale
		g.append(a[4])					#PG 2018
		g.append(a[5])					#MV 2018
		g.append(a[6])					#MF 2018
		g.append(int(a[8]) + int(a[17]))#GS 2018
		g.append(a[9])					#RP 2018
		g.append(a[15])					#AM 2018
		g.append(a[16])					#ES 2018
		
		for item in p17:
			if a[2] == item[2]:
				g.append(item[3])						#Squadra vecchia
				g.append(item[4])						#PG 2017
				g.append(item[5])						#MV 2017
				g.append(item[6])						#MF 2017
				g.append(int(item[8]) + int(item[17]))	#GS 2018
				g.append(item[9])						#RP 2018
				g.append(item[15])						#AM 2018
				g.append(item[16])						#ES 2018
		#print g
		op.append(g)

	with open('portieri.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(["Nome", "Squadra", "PG", "MV", "MF", "GS", "RP", "AM", "ES", "2017","PG", "MV", "MF", "GS", "RP", "AM", "ES"])
		
		for row in op:
			spamwriter.writerow(row)

	while d18:
		g = []
		a = d18.pop()
		g.append(a[2])						#Nome
		g.append(a[3])						#Squadra attuale
		g.append(a[4])						#PG 2018
		g.append(a[5])						#MV 2018
		g.append(a[6])						#MF 2018
		g.append(a[7])						#GF 2018
		g.append(a[10])						#RC 2018
		g.append(a[11])						#R+ 2018
		g.append(a[12])						#R- 2018
		g.append(int(a[13]) + int(a[14]))	#AS 2018
		g.append(a[15])						#AM 2018
		g.append(a[16])						#ES 2018
		g.append(a[17])						#AU 2018
		
		for item in d17:
			if a[2] == item[2]:
				g.append(item[3])						#Squadra vecchia
				g.append(item[4])						#PG 2018
				g.append(item[5])						#MV 2018
				g.append(item[6])						#MF 2018
				g.append(item[7])						#GF 2018
				g.append(item[10])						#RC 2018
				g.append(item[11])						#R+ 2018
				g.append(item[12])						#R- 2018
				g.append(int(item[13]) + int(item[14]))	#AS 2018
				g.append(item[15])						#AM 2018
				g.append(item[16])						#ES 2018
				g.append(item[17])						#AU 2018
				
		for item in c17:
			if a[2] == item[2]:
				g.append(item[3])						#Squadra vecchia
				g.append(item[4])						#PG 2018
				g.append(item[5])						#MV 2018
				g.append(item[6])						#MF 2018
				g.append(item[7])						#GF 2018
				g.append(item[10])						#RC 2018
				g.append(item[11])						#R+ 2018
				g.append(item[12])						#R- 2018
				g.append(int(item[13]) + int(item[14]))	#AS 2018
				g.append(item[15])						#AM 2018
				g.append(item[16])						#ES 2018
				g.append(item[17])						#AU 2018
				
		for item in a17:
			if a[2] == item[2]:
				g.append(item[3])						#Squadra vecchia
				g.append(item[4])						#PG 2018
				g.append(item[5])						#MV 2018
				g.append(item[6])						#MF 2018
				g.append(item[7])						#GF 2018
				g.append(item[10])						#RC 2018
				g.append(item[11])						#R+ 2018
				g.append(item[12])						#R- 2018
				g.append(int(item[13]) + int(item[14]))	#AS 2018
				g.append(item[15])						#AM 2018
				g.append(item[16])						#ES 2018
				g.append(item[17])						#AU 2018
		
		od.append(g)

	with open('difensori.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(["Nome", "Squadra", "PG", "MV", "MF", "GF", "RC", "R+", "R-", "AS", "AM", "ES", "AU", "2017","PG", "MV", "MF", "GF", "RC", "R+", "R-", "AS", "AM", "ES", "AU"])
		
		for row in od:
			spamwriter.writerow(row)

	while c18:
		g = []
		a = c18.pop()
		g.append(a[2])						#Nome
		g.append(a[3])						#Squadra attuale
		g.append(a[4])						#PG 2018
		g.append(a[5])						#MV 2018
		g.append(a[6])						#MF 2018
		g.append(a[7])						#GF 2018
		g.append(a[10])						#RC 2018
		g.append(a[11])						#R+ 2018
		g.append(a[12])						#R- 2018
		g.append(int(a[13]) + int(a[14]))	#AS 2018
		g.append(a[15])						#AM 2018
		g.append(a[16])						#ES 2018
		g.append(a[17])						#AU 2018
		
		for item in d17:
			if a[2] == item[2]:
				g.append(item[3])						#Squadra vecchia
				g.append(item[4])						#PG 2018
				g.append(item[5])						#MV 2018
				g.append(item[6])						#MF 2018
				g.append(item[7])						#GF 2018
				g.append(item[10])						#RC 2018
				g.append(item[11])						#R+ 2018
				g.append(item[12])						#R- 2018
				g.append(int(item[13]) + int(item[14]))	#AS 2018
				g.append(item[15])						#AM 2018
				g.append(item[16])						#ES 2018
				g.append(item[17])						#AU 2018
				
		for item in c17:
			if a[2] == item[2]:
				g.append(item[3])						#Squadra vecchia
				g.append(item[4])						#PG 2018
				g.append(item[5])						#MV 2018
				g.append(item[6])						#MF 2018
				g.append(item[7])						#GF 2018
				g.append(item[10])						#RC 2018
				g.append(item[11])						#R+ 2018
				g.append(item[12])						#R- 2018
				g.append(int(item[13]) + int(item[14]))	#AS 2018
				g.append(item[15])						#AM 2018
				g.append(item[16])						#ES 2018
				g.append(item[17])						#AU 2018
				
		for item in a17:
			if a[2] == item[2]:
				g.append(item[3])						#Squadra vecchia
				g.append(item[4])						#PG 2018
				g.append(item[5])						#MV 2018
				g.append(item[6])						#MF 2018
				g.append(item[7])						#GF 2018
				g.append(item[10])						#RC 2018
				g.append(item[11])						#R+ 2018
				g.append(item[12])						#R- 2018
				g.append(int(item[13]) + int(item[14]))	#AS 2018
				g.append(item[15])						#AM 2018
				g.append(item[16])						#ES 2018
				g.append(item[17])						#AU 2018
		oc.append(g)

	with open('centrocampisti.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(["Nome", "Squadra", "PG", "MV", "MF", "GF", "RC", "R+", "R-", "AS", "AM", "ES", "AU", "2017","PG", "MV", "MF", "GF", "RC", "R+", "R-", "AS", "AM", "ES", "AU"])
		
		for row in oc:
			spamwriter.writerow(row)

	while a18:
		g = []
		a = a18.pop()
		g.append(a[2])						#Nome
		g.append(a[3])						#Squadra attuale
		g.append(a[4])						#PG 2018
		g.append(a[5])						#MV 2018
		g.append(a[6])						#MF 2018
		g.append(a[7])						#GF 2018
		g.append(a[10])						#RC 2018
		g.append(a[11])						#R+ 2018
		g.append(a[12])						#R- 2018
		g.append(int(a[13]) + int(a[14]))	#AS 2018
		g.append(a[15])						#AM 2018
		g.append(a[16])						#ES 2018
		g.append(a[17])						#AU 2018
		
		for item in d17:
			if a[2] == item[2]:
				g.append(item[3])						#Squadra vecchia
				g.append(item[4])						#PG 2018
				g.append(item[5])						#MV 2018
				g.append(item[6])						#MF 2018
				g.append(item[7])						#GF 2018
				g.append(item[10])						#RC 2018
				g.append(item[11])						#R+ 2018
				g.append(item[12])						#R- 2018
				g.append(int(item[13]) + int(item[14]))	#AS 2018
				g.append(item[15])						#AM 2018
				g.append(item[16])						#ES 2018
				g.append(item[17])						#AU 2018
				
		for item in c17:
			if a[2] == item[2]:
				g.append(item[3])						#Squadra vecchia
				g.append(item[4])						#PG 2018
				g.append(item[5])						#MV 2018
				g.append(item[6])						#MF 2018
				g.append(item[7])						#GF 2018
				g.append(item[10])						#RC 2018
				g.append(item[11])						#R+ 2018
				g.append(item[12])						#R- 2018
				g.append(int(item[13]) + int(item[14]))	#AS 2018
				g.append(item[15])						#AM 2018
				g.append(item[16])						#ES 2018
				g.append(item[17])						#AU 2018
				
		for item in a17:
			if a[2] == item[2]:
				g.append(item[3])						#Squadra vecchia
				g.append(item[4])						#PG 2018
				g.append(item[5])						#MV 2018
				g.append(item[6])						#MF 2018
				g.append(item[7])						#GF 2018
				g.append(item[10])						#RC 2018
				g.append(item[11])						#R+ 2018
				g.append(item[12])						#R- 2018
				g.append(int(item[13]) + int(item[14]))	#AS 2018
				g.append(item[15])						#AM 2018
				g.append(item[16])						#ES 2018
				g.append(item[17])						#AU 2018
		
		oa.append(g)

	with open('attaccanti.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(["Nome", "Squadra", "PG", "MV", "MF", "GF", "RC", "R+", "R-", "AS", "AM", "ES", "AU", "2017","PG", "MV", "MF", "GF", "RC", "R+", "R-", "AS", "AM", "ES", "AU"])
		
		for row in oa:
			spamwriter.writerow(row)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
