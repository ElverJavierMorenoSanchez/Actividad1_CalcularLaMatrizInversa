import numpy as np

#Variables
matriz = []
arr = np.array([])

#Calcular el determinante
def inputMatriz():
    for i in range(2):
        matriz.append([0] * 2)

    for i in range(2):
        for j in range(2):
            matriz[i][j] = int(input('Introduce el valor de la posicion [{}][{}]: '.format(i, j)))

    return np.array(matriz)

def calDeterminante(arr):
    det = (arr[0][0] * arr[1][1]) - (arr[0][1] * arr[1][0])

    return det
