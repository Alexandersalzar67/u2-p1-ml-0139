import numpy as np
print(" - - - - llenar matriz de ceros - - - -")
matriz=np.zeros([3,5]) # 3 filas x 5 columnas
print(matriz)
print(" - - - - llenar matriz de unos - - - -")
matriz=np.ones([3,5])
print(matriz)
print(" - - - - llenar matriz de vacios- - - -")
matriz=np.empty([3,5])
print(matriz)
print(" - - - - llenar lista con rango- - - -")
#el primer parametro es el valor oficial
#el segundo parametro es el valor inicial
#el tercero paramento es el incremento
lista=np.arange(0,10,2)
print(lista)