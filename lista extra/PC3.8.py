""" Resolução da questão PC3.8 """

import control as ctrl
import numpy as np


# Função que calcula os autovalores
def calcular_autovalores(K):
    A = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [-2,-K,-2]])
    autovalores = np.linalg.eigvals(A)
    return autovalores

# Definindo K
valores_K = np.linspace(0,100,1000)

autovalores = 