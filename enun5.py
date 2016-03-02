#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 5. Pide por teclado el nombre 
# de un hotel y te devuelva su pagina web (Nota: casi todos los nombres de los hoteles empiezan por el numero de * que 
# tienen y algunos hoteles no disponen de página web)

import json

with open("hoteles.json") as fichero:
	datos = json.load(fichero)

var = raw_input("Nombre del hotel o que empiece por tal cadena: ").title()

#Recorrer y dejar los nombres sin las estrellas de delante
#Almacenarlos en un diccionario

hoteles = {}

for d in datos["resources"]:
	if d["dc:title"].count("*") == 5:
		d["dc:title"] = d["dc:title"].lstrip("***** ")
		key = d["dc:title"] 
		value = d["lpgc:web"]
		hoteles[key] = value
	elif d["dc:title"].count("*") == 4:
		d["dc:title"] = d["dc:title"].lstrip("**** ")
		key = d["dc:title"] 
		value = d["lpgc:web"]
		hoteles[key] = value
	elif d["dc:title"].count("*") == 3:
		d["dc:title"] = d["dc:title"].lstrip("*** ")
		key = d["dc:title"] 
		value = d["lpgc:web"]
		hoteles[key] = value
	elif d["dc:title"].count("*") == 2:
		d["dc:title"] = d["dc:title"].lstrip("** ")
		key = d["dc:title"] 
		value = d["lpgc:web"]
		hoteles[key] = value
	elif d["dc:title"].count("*") == 1:
		d["dc:title"] = d["dc:title"].lstrip("* ")
		key = d["dc:title"] 
		value = d["lpgc:web"]
		hoteles[key] = value
	else:
		key = d["dc:title"] 
		value = d["lpgc:web"]
		hoteles[key] = value

#Buscar si la variable coincide con una key y mostrar su value = urls
	
for k, v in hoteles.items():
	if k.startswith(var) and v == "":
		print ""
		print "La url del sitio web del hotel " + k + " --> " + "No esta disponible"
		print ""
	elif k.startswith(var) and v != "":
		print ""
		print "La url del sitio web del hotel " + k + " --> " + v
		print ""

