#! /usr/bin/env python
# -*- coding：utf-8 -*-
# Author : Yuan
import json

info= {'name':'yuan','age':22}

f =  open("text.text","w")

# f.write(str(info))

f.write(json.dumps(info))

f.close()