#! /usr/bin/env python
# -*- coding：utf-8 -*-
# Author : Yuan


import json

f = open("text.text","r")

print(json.loads(f.read()))




