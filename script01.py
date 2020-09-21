# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:48:59 2020

@author: Zamora
"""


#listas en python
lista = [1,-0.5, 3, -8.2]

#ordenar lista
lista.sort()

#invertir lista
lista.reverse()

#vector de entrada
x = [1.0, 8.0, 4.4, 7.5, 9.9]

#pesos sinapticos
w = [-0.5, 1.0, 0.8, -0.7, 2.5]

#importar numpy
import numpy as np
#convertir una lista en un vector de numpy
np.array(x)
np.array(w)
#producto interno con for
'''
for i in range(0,5):
    print(i)
'''
productoInterno = 0    
for i in range(0, len(w)):
    productoInterno = productoInterno + w[i]*x[i]
print(productoInterno)

#producto interno con numpy
np.dot(w,x)
#calcular la salida de una neurona con 
#funcion de activasion tangente hiperbolica
np.tanh(np.dot(w,x))
    