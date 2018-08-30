#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generatore.py
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
import sys
import random

def main(args):
	filex = open("database.csv", "w")
	tipo = ["1", "2", "3", "4"]
	oggetti = ["freno", "gancio", "fascia", "asse", "sterzo", "braccetto", "portiera", "cofano", "giravite", "frigo a legna"]
	fornitori = ["pippo a tivoli", "franco franchi", "ciccio ingrassia", "christian de sica", "gigi proietti"]
	marche = ["brembo", "barilla", "LIDL", "magneti marelli", "cinesi" ]
	descrizione = ["Lorem Ipsum", "Dolor sit Amet", "42 è la risposta", "Maurizio che non diventi un vizio", "333 123 456 bella li"]
	for i in range(1, 301):
		a = "1," + str(i) + "," + random.choice(oggetti) + "," + random.choice(descrizione) + "\n"
		filex.write(a)
	
	for i in range(301, 901):
		a = "2," + str(i) + "," + random.choice(fornitori) + "," + random.choice(descrizione) + "\n"
		filex.write(a)

	for i in range(901, 1301):
		a = "3," + str(i) + "," + random.choice(marche) + "," + random.choice(descrizione) + "\n"
		filex.write(a)

	for i in range(1301, 4000):
		a = "4," + str(i) + "," + str(random.randint(1, 130)) + "," + str(random.randint(1, 130)) + "\n"
		filex.write(a)
		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
