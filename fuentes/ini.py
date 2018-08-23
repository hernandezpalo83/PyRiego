#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
from holamundo import f_holamundo
from blik import f_blik
import variables
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Encender/Apagar")
	print ("\t2 - Sin funcion")
	print ("\t3 - Sin funcion")
	print ("\t9 - salir")
    
 
while True:
    print ("MENU")
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
    
	if opcionMenu=="1":
		f_blik(True)        
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")