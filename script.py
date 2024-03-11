from math import *

#input des valeurs de a, b et c
a = float(input("entrez a: "))
b = float(input("entrez b: "))
c = float(input("entrez c: "))

#calcul de delta
delta1 = b*b
delta2 = 4*a*c
delta = delta1-delta2

#calcul des racines
if delta<=0 :
	print(f"le polynôme n'a pas de racine car delta = {delta} < 0")
	
if delta == 0:
	x1 = -1*b
	x2 = 2*a
	x0 = x1/x2
	print(f"la racine du polynome est: {x0}, son delta est {delta}")
	
if delta >=0:
	x11 = -1*b
	x12 = sqrt(delta)
	x13 = x11-x12
	x14 = x11+x12
	x15 = 2*a
	x1 = x13/x15
	x2 = x14/x15
	print(f"les racines du polynome sont: {x1} et {x2}, son delta est {delta}")
