import numpy as np

califas=np.array([60,70,90])
print("-++-+-+-ej 1 imprimir califas+--+-+--+-+")
print(califas) # imprime la lista de califas
print(type(califas)) # muestra el tipo de de arreglo
print("-++-+-+-ej 2 imprimir califas+--+-+--+-+")
califas=np.array(60)
print(califas)
print("Dimension :", califas.ndim)
print("-++-+-+-ej 1 dimensiones de un array +--+-+--+-+")
califas=np.array([60,70,90])
print(califas)
print("dimension :", califas.ndim)
print("-++-+-+-ej 2 dimensiones de un array +--+-+--+-+")
califas=np.array([
    [60,70,90]
    [50,80,98]
    ]) #  un arreglo de 2 dimensiones  es como unatabla de excel
print(califas)
print("dimension :", califas.ndim)
