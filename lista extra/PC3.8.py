""" Resolução da questão PC3.8 """

import control as ctrl
import numpy as np

# Definindo K
K = np.linspace(0,100,1000)

# Matriz EE
A = np.array([[0,1,0],[0,0,1],[-2,-K,-2]])

