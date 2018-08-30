#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fornitori.py
#  
#  Copyright 2018 Emanuele Savo <tucs@Lyra>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

import csv
def doom():
	print """
+-----------------------------------------------------------------------------+
| |       |\                                           -~ /     \  /          |
|~~__     | \                                         | \/       /\          /|
|    --   |  \                                        | / \    /    \     /   |
|      |~_|   \                                   \___|/    \/         /      |
|--__  |   -- |\________________________________/~~\~~|    /  \     /     \   |
|   |~~--__  |~_|____|____|____|____|____|____|/ /  \/|\ /      \/          \/|
|   |      |~--_|__|____|____|____|____|____|_/ /|    |/ \    /   \       /   |
|___|______|__|_||____|____|____|____|____|__[]/_|----|    \/       \  /      |
|  \mmmm :   | _|___|____|____|____|____|____|___|  /\|   /  \      /  \      |
|      B :_--~~ |_|____|____|____|____|____|____|  |  |\/      \ /        \   |
|  __--P :  |  /                                /  /  | \     /  \          /\|
|~~  |   :  | /                                 ~~~   |  \  /      \      /   |
|    |      |/                        .-.             |  /\          \  /     |
|    |      /                        |   |            |/   \          /\      |
|    |     /                        |     |            -_   \       /    \    |
+-----------------------------------------------------------------------------+
|          |  /|  |   |  2  3  4  | /~~~~~\ |       /|    |_| ....  ......... |
|          |  ~|~ | % |           | | ~J~ | |       ~|~ % |_| ....  ......... |
|   AMMO   |  HEALTH  |  5  6  7  |  \===/  |    ARMOR    |#| ....  ......... |
+-----------------------------------------------------------------------------+


Doom!"""
	raw_input()
	
def print2(ogt):
	while True:
		os.system('clear')
		print color.BOLD + "\n\n\t[Analisi #" + str(ogt[1]) + " - " + str(ogt[2]) + "]" + color.END 
		if str(ogt[0]) == "1":
			print color.BOLD + "\nTipo:\t\t"+ color.END +"Oggetto"
		if str(ogt[0]) == "2":
			print color.BOLD + "\nTipo:\t\t"+ color.END +"Fornitore"
		if str(ogt[0]) == "3":
			print color.BOLD + "\nTipo:\t\t"+ color.END +"Marca"
		print color.BOLD + "\nNome:\t\t" + color.END + str(ogt[2])
		print color.BOLD + "\nDescrizione:\t" + color.END + str(ogt[3])
	
		print color.UNDERLINE + "\nOggetti collegati:" + color.END
		for i in range(0, len(collegamenti)):
			if int(collegamenti[i][2]) == int(ogt[1]):
				for j in range(0, len(listato)):
					if str(listato[j][0]) == str(1):
						if str(listato[j][1]) == str(collegamenti[i][3]):
							print "\t\t" + listato[j][1] + "\t" + listato[j][2]
			if int(collegamenti[i][3]) == int(ogt[1]):
				for j in range(0, len(listato)):
					if str(listato[j][0]) == str(1):
						if str(listato[j][1]) == str(collegamenti[i][2]):
							print "\t\t" + listato[j][1] + "\t" + listato[j][2]

		print color.UNDERLINE + "\n\nFornitori collegati:" + color.END
		for i in range(0, len(collegamenti)):
			if int(collegamenti[i][2]) == int(ogt[1]):
				for j in range(0, len(listato)):
					if str(listato[j][0]) == str(2):
						if str(listato[j][1]) == str(collegamenti[i][3]):
							print "\t\t" + listato[j][1] + "\t" + listato[j][2]
			if int(collegamenti[i][3]) == int(ogt[1]):
				for j in range(0, len(listato)):
					if str(listato[j][0]) == str(2):
						if str(listato[j][1]) == str(collegamenti[i][2]):
							print "\t\t" + listato[j][1] + "\t" + listato[j][2]

		print color.UNDERLINE + "\n\nMarche collegate:" + color.END
		for i in range(0, len(collegamenti)):
			if int(collegamenti[i][2]) == int(ogt[1]):
				for j in range(0, len(listato)):
					if str(listato[j][0]) == str(3):
						if str(listato[j][1]) == str(collegamenti[i][3]):
							print "\t\t" + listato[j][1] + "\t" + listato[j][2]
			if int(collegamenti[i][3]) == int(ogt[1]):
				for j in range(0, len(listato)):
					if str(listato[j][0]) == str(3):
						if str(listato[j][1]) == str(collegamenti[i][2]):
							print "\t\t" + listato[j][1] + "\t" + listato[j][2]
			
		a = raw_input("""
.-------------------------------.
| Invio\tTorna indietro
| Q\tTorna al menu principale
|		
| Altrimenti inserire n° elemento
'---------------------------------> """)
		if ((a =="q") or (a == "Q")) :
			return 10
		if not a:
			break
		for i in range(0, len(listato)):
			#print alist[i][1]
			if str(listato[i][1]) == str(a):
				if (print2(listato[i]) == 10):
					return 10
				break
				
def print1(alist, strng):
	while True:
		os.system('clear')
		print color.BOLD + "\n\t\t[Lista " + str(strng) + "]\n" + color.END
		for i in range(0, len(alist)):
			print "\n\n\t" + color.UNDERLINE + str(alist[i][1]) + "\t" +  str(alist[i][2]) + color.END
			print "\t\t" + str(alist[i][3])
	
		a = raw_input("""
.-------------------------------.
| Invio\tTorna indietro
| Q\tTorna al menu principale
|		
| Altrimenti inserire n° elemento
'---------------------------------> """)
		if ((a =="q") or (a == "Q")) :
			return 10
		if not a:
			break
		for i in range(0, len(alist)):
			#print alist[i][1]
			if str(alist[i][1]) == str(a):
				if (print2(alist[i]) == 10):
					return 10
				break
			
def searchv(idval, cercstr):
	while True:
		os.system('clear')
		a = str(raw_input(color.BOLD + "\n\n\t[" + cercstr + "]: " + color.END))
		aa = a.upper()

		if (int(idval) == 1) or idval == 0 :
			if idval == 0:
				print color.BOLD + "\n\t[OGGETTI]" + color.END
			for i in range(0, len(listato)):
				bb = listato[i][2].upper().split()
				bc = listato[i][3].upper().split()
				if int(listato[i][0]) == 1:
					if ((aa in bb) or (aa in bc)):
						print color.UNDERLINE + "\n\t" + str(listato[i][1]) + color.END + "\t" + str(listato[i][2]) + "\n\t\t\t" + str(listato[i][3])

		if (int(idval) == 2) or idval == 0 :
			if idval == 0:
				print color.BOLD + "\n\t[FORNITORI]" + color.END
			for i in range(0, len(listato)):
				bb = listato[i][2].upper().split()
				bc = listato[i][3].upper().split()
				if int(listato[i][0]) == 2:
					if ((aa in bb) or (aa in bc)):
						print color.UNDERLINE + "\n\t" + str(listato[i][1]) + color.END + "\t" + str(listato[i][2]) + "\n\t\t\t" + str(listato[i][3])

		if (int(idval) == 3) or idval == 0 :
			if idval == 0:
				print color.BOLD + "\n\t[MARCHE]" + color.END
			for i in range(0, len(listato)):
				bb = listato[i][2].upper().split()
				bc = listato[i][3].upper().split()
				if int(listato[i][0]) == 3:
					if ((aa in bb) or (aa in bc)):
						print color.UNDERLINE + "\n\t" + str(listato[i][1]) + color.END + "\t" + str(listato[i][2]) + "\n\t\t\t" + str(listato[i][3])
	
		a = raw_input("""
.-------------------------------.
| Invio\tTorna indietro
| Q\tTorna al menu principale
|		
| Altrimenti inserire n° elemento
'---------------------------------> """)
		if ((a =="q") or (a == "Q")) :
			return 10
		if not a:
			break
		for i in range(0, len(listato)):
			#print alist[i][1]
			if str(listato[i][1]) == str(a):
				if (print2(listato[i]) == 10):
					return 10
				break

def mainmenu():
	#Stampa Fornitori
	os.system('clear')
	#os.system('cls')
	print color.BOLD + color.BLUE + "\n         _____      _ ____            _ " + color.DARKCYAN + "\n        / ___/_____(_) __/___  ____  (_)" + color.CYAN + "\n        \__ \/ ___/ / /_/ __ \/ __ \/ / " + color.GREEN + "\n       ___/ / /__/ / __/ /_/ / / / / /  "+ color.YELLOW + "\n      /____/\___/_/_/  \____/_/ /_/_/  _    _  " + color.RED + "\n __ _ _  _| |_ ___ _ _(_)__ __ _ _ __ | |__(_)" + color.PURPLE + "\n/ _` | || |  _/ _ \ '_| / _/ _` | '  \| '_ \ |"+ color.END + "\n\__,_|\_,_|\__\___/_| |_\__\__,_|_|_|_|_.__/_|" + color.END

	print color.BOLD + "\n\n\t[Menu Principale]" + color.END
	print "\n"
	print "\t[1]\tMostra Oggetti"
	print "\t[2]\tMostra Fornitori"
	print "\t[3]\tMostra Marche"
	print ""
	print "\t[4]\tCerca"
	print "\t[5]\tCerca per Oggetto"
	print "\t[6]\tCerca per Fornitore"
	print "\t[7]\tCerca per Marca"
	print ""
	print "\t[Q]\tEsci da questo meraviglioso programma"
	print ""
	
def main(args):
    return 0

if __name__ == '__main__':
	
    import sys
    import os
    oggetti = []
    fornitori = []
    marche = []
    collegamenti = []
    listato = []
    with open('ScifoniAutoricambi.csv', 'rb') as csvfile:
		leggi = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in leggi:
			#print row
			listato.append(row)
			if row[0] == '1':
				oggetti.append(row)
			if row[0] == '2':
				fornitori.append(row)
			if row[0] == '3':
				marche.append(row)
			if row[0] == '4':
				collegamenti.append(row)
    while True:
		mainmenu()
		a = str(raw_input("Inserire comando: "))
		if a == "1":
			print1(oggetti, "Oggetti")
		elif a == "2":
			print1(fornitori, "Fornitori")
		elif a == "3":
			print1(marche, "Marche")
		elif a == "dc":
			print1(collegamenti, "Collegamenti")
		elif a == "doom":
			doom()
		elif a == "4":
			searchv(0, "Cerca")
		elif a == "5":
			searchv(1, "Cerca per oggetto")
		elif a == "6":
			searchv(2, "Cerca per fornitore")
		elif a == "7":
			searchv(3, "Cerca per marca")
		elif a == "Q" or a =="q":
			break
