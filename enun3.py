#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3. Los hoteles estan organizados en 3 categorias de precios, pide una categoria y muestra los correspondientes hoteles de ese precio

import json

with open("hoteles.json") as fichero:
	datos = json.load(fichero)

# alto, medio o Precio medio, Económico o " Precio Económico" 

var = raw_input("Introduce(caro, normal o barato): ")

caros = []
normales = []
baratos = []

for d in datos["resources"]:
	if d["lpgc:precio"] == "alto" or d["lpgc:precio"] == "Alto":
		caros.append(d["dc:title"])

	if d["lpgc:precio"] == "medio" or d["lpgc:precio"] == "Precio medio":
		normales.append(d["dc:title"])

	if d["lpgc:precio"].encode('utf-8') == "Económico" or d["lpgc:precio"].encode('utf-8') == " Precio Económico":
		baratos.append(d["dc:title"])


if var == "caro":
	for c in caros:
		print c
elif var == "normal":
	for n in normales:
		print n
elif var == "barato":
	for b in baratos:
		print b
else:
	print "No ha introducido bien la opción"