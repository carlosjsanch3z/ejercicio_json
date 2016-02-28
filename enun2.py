#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2.Muestra el número de hoteles que existen por numeros de estrellas que tengan

import json

with open("/home/charlie/Escritorio/GitHub/ejercicio_json/hoteles.json") as fichero:
	datos = json.load(fichero)

fivestarts = 0
fourstarts = 0 
threestarts = 0
twostarts = 0
onestart = 0

for d in datos["resources"]:
	if d["dc:title"].count("*") == 5:
		fivestarts += 1
	if d["dc:title"].count("*") == 4:
		fourstarts += 1
	if d["dc:title"].count("*") == 3:
		threestarts += 1
	if d["dc:title"].count("*") == 2:
		twostarts += 1
	if d["dc:title"].count("*") == 1:
		onestart += 1


print "Hoteles de 5 estrellas: " + str(fivestarts)
print "Hoteles de 4 estrellas: " + str(fourstarts)
print "Hoteles de 3 estrellas: " + str(threestarts)
print "Hoteles de 2 estrellas: " + str(twostarts)
print "Hoteles de 1 estrella: " + str(onestart)