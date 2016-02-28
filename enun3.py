#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3. Los hoteles estan organizados en 3 categorias de precios, pide una categoria y muestra los correspondientes hoteles de ese precio

import json

with open("/home/charlie/Escritorio/GitHub/ejercicio_json/hoteles.json") as fichero:
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

	if d["lpgc:precio"] == "Económico" or d["lpgc:precio"] == " Precio Económico":
		baratos.append(d["dc:title"])

for n in baratos:
	print n