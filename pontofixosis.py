#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def func1(x):
 return 1./3*np.cos(x[1]*x[2]) + 1/6.

def func2(x):
 return 1/9.*(x[0]**2+np.sin(x[2])+1.06)**0.5-0.1

def func3(x):
 return -1/20.*np.exp(-x[0]*x[1])-(10*np.pi-3)/60

funcs=[func1, func2, func3]

x=[1,-1,1]
ox=[0,0,0]
cont=0
while((ox[0]-x[0])**2+(ox[1]-x[1])**2+(ox[2]-x[2])**2>0.01):
 ox=np.copy(x)
 for i in xrange(0,3):
  x[i]=funcs[i](x)
 cont=cont+1

print x,cont
  
