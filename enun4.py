#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 4. Pide por teclado los dos últimos numeros del telefono y que 
# muestre una lista de los telefonos que coinciden acabados en esos dos numeros junto al nombre del hotel al que corresponde

import json

with open("hoteles.json") as fichero:
	datos = json.load(fichero)


var = raw_input("Los dos últimos números del telefono: ")

for d in datos["resources"]:
	if d["lpgc:telefono"][-2:] == var:
		print d["dc:title"] + "  " + d["lpgc:telefono"]
	