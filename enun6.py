#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 6. Genera un fichero index.html
#<h1> Nombre
#<p> Dirección
#<a href=url

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json

lista = []
dicc = {}

with open("hoteles.json") as fichero:
	datos = json.load(fichero)

for d in datos["resources"]:
	hotel = d["dc:title"]
	address = d["lpgc:direccion"]
	lat = d["geo:lat"]
	log = d["geo:long"]
	url = "http://www.openstreetmap.org/way/109089302#map=17/" + str(lat) + "/" + str(log)
	
	dicc["hotel"]=hotel
	dicc["address"]=address
	dicc["url"]=url
	lista.append(dicc)
	dicc = {}


with open ("index.html", "w") as archivo:

	for elemento in lista:
		archivo.write("<h1>"+elemento["hotel"]+"</h1>"+"\n")
		archivo.write("<p>"+elemento["address"]+"</p>"+"\n")
		archivo.write("<a href="+str(elemento["url"])+">"+"Mapa"+"</a>"+"\n")
