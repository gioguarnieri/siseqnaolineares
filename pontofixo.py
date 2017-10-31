#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

func=np.cos

x=10300
cont=0

while abs(x-func(x))>0.000000000001:
 x=func(x)
 cont=cont+1

print x, cont
