#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def func1(a):
 return a[0]**2-81*(a[1]+0.1)**2+np.sin(a[2])+1.06

def func2(a):
 return np.exp(a[0]*a[1])+20*a[2]+(10*np.pi-3)/3
def func3(a):
 return 3*a[0]-np.cos(a[1]*a[2])-1./2

def dfunc(func,x,i):
 a=np.copy(x)
 b=np.copy(x)
 a[i]=a[i]+h/2
 b[i]=b[i]-h/2
 return (func(a)-func(b))/h

funcs=[func1, func2, func3]

h=1e-3
x=[0.1,0.1,-0.1]
ox=[0,0,0]
F=[0.,0.,0.]
y=[0.,0.,0.]
jacob=np.zeros((len(x),len(x)),float)

while((ox[0]-x[0])**2+(ox[1]-x[1])**2+(ox[2]-x[2])**2>1e-10):
 ox=np.copy(x)
 for i in xrange(0,3):
  F[i]=-funcs[i](x)
  for j in xrange(0,3):
   jacob.itemset((i,j),dfunc(funcs[i],x,j))

 for i in xrange(0,3):
  for j in xrange(0,3):
   y[i]=y[i]-F[j]/jacob.item(i,j)
  x[i]=x[i]+y[i]
 print x

print x
