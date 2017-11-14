#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import sys

## FUNÇÕES DO GAUSS JORDAN ##

def Escalona(x,resp):
 lu=np.zeros((n+1,n+1), float)
 resp2=np.zeros(n, float)
 resp2=resp
 lamda=[]
 moddet=0
 op=0
 for tt in xrange(0, n):
  for t in xrange(tt+1,n):
   #if abs(x.item(tt,tt))<abs(x.item(t,tt)):
   # moddet=moddet+1
   # y=np.copy(x[tt])
   # x[tt]=np.copy(x[t])
   # x[t]=np.copy(y)
   #op=op+2+n
   lamda.append(x.item(t,tt)/x.item(tt,tt))
   resp2[t]=resp2[t]-lamda[-1]*resp2[tt]
   x[t]=np.copy(x[t]-lamda[-1]*x[tt])
   lu.itemset((t,tt),lamda[-1])
 for i in xrange(0,n+1):
  lu.itemset((i,i),1)
 return x,lamda,op,resp2,lu



def CalculoDet(x):
 det=1
 for i in xrange(0,n):
  det=det*x.item(i,i)
 return det



def Substitui(x,resp2):
 y=resp2
 for i in xrange(n-1,-1,-1):
  j=n-1
  while (j>i):
   y[i]=y[i]-x.item(i,j)*y[j]
   j=j-1
  y[i]=y[i]/x.item(i,i)
 return y

def Coeficientes(z,y):
 w=np.zeros([n], float)
 for tt in xrange(0,n):
  for t in xrange(0,n):
   w[tt]=np.copy(w[tt]+y[t]*z.item(tt,t))
 return w

def FazTudo(x,resp):
 lu=np.zeros((len(x)+1,len(x)+1), float)
 z=np.copy(x)
 n=len(x)+1
 moddet=0
 x,l,op,resp2,lu=Escalona(x,resp)
 det=CalculoDet(x)
 y=Substitui(x,resp2)
 simply=[ round(elem,2) for elem in y ]
 w=Coeficientes(z,y)
 return simply


## FUNÇÕES PARA GERAR O SISTEMA E O JACOBIANO ##
filewrite=open(sys.argv[4], 'w')

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
x=[float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])]
ox=[0,0,0]
F=[0.,0.,0.]
y=[0.,0.,0.]
n=len(x)
jacob=np.zeros((n,n+1),float)
ii=0
print "Valores tentativos:"
while((ox[0]-x[0])**2+(ox[1]-x[1])**2+(ox[2]-x[2])**2>1e-10 and ii<15):
 ii=ii+1
 ox=np.copy(x)
 for i in xrange(0,3):
  F[i]=-funcs[i](x)
  for j in xrange(0,3):
   jacob.itemset((i,j),dfunc(funcs[i],x,j))
 for i in xrange(0,3):
  jacob.itemset((i,3), F[i])
 
 y=FazTudo(jacob,F)
 print "Mudanças dos valores em x"
 print y
 filewrite.write(str(y[0]**2+y[1]**2+y[2]**2) + '    ' + str(ii) + '\n')
 
 for i in xrange(0,len(y)):
  x[i]=x[i]+y[i]
 print "Raízes atualizadas"
 print x

print "Norma do vetor"
print x[0]**2+x[1]**2+x[2]**2

print "Quantidade de passos"
print ii

print "Resultado final"
print x
