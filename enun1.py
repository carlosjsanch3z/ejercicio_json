#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Lista solamente los hoteles que tengan 4 estrellas

import json

with open("hoteles.json") as fichero:
	datos = json.load(fichero)

for d in datos["resources"]:
	if d["dc:title"][0:5] == "**** ":
		print d["dc:title"]