#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def func(x):
 return np.cos(x)-x

def dfunc(x):
 return (func(x+h)-func(x))/h

h=1e-3
tol=1e-10
x=1
ox=0
i=0
while((ox-x)**2>tol):
 ox=x
 x=x-func(x)/dfunc(x)
 i=i+1

print x,i
