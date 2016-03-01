#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 5. Pide por teclado el nombre 
# de un hotel y te devuelva su pagina web (Nota: casi todos los nombres de los hoteles empiezan por el numero de * que tienen )

import json

with open("hoteles.json") as fichero:
	datos = json.load(fichero)

var = raw_input("Nombre del hotel o que empiece por tal cadena: ")

#Recorrer y dejar los nombres sin sus estrellas
for d in datos["resources"]:
	if d["dc:title"].count("*") == 5:
		d["dc:title"] = d["dc:title"].lstrip("*****")
		if d["dc:title"].startswith(var):
			print d["dc:title"]


#Almacenarlos en una lista o diccionario



#Buscar si la variable coincide con una key y mostrar su value = url