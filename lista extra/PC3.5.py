""" Resolução da questão PC3.5"""

import control as ctrl
import numpy as np

# Criando função de arredondamento para evitar erro computacional
def arredondar(FT):
    FT.num = [[FT.num[0][0].round(6)]]
    return FT

# Definindo as matrizes de estado do sistema 1
A1 = np.array([[0,1,0],[0,0,1],[-4,-5,-8]])
B1 = np.array([[0],[0],[4]])
C1 = np.array([[1,0,0]])
D1 = np.array([[0]])

# Sistema 1 é dado por
sist_ss1 = ctrl.StateSpace(A1,B1,C1,D1)

# Transformando Espaço de estado em FT e arredondando numerador
G1 = ctrl.ss2tf(sist_ss1)
G1 = arredondar(G1)

# Printando resposta letra (a)
print(f'(a)\n{G1}')

# Definindo as matrizes de estado do sistema 2
A2 = np.array([[0.5,0.5,0.7071],[-0.5,-0.5,0.7071],[-6.3640,-0.7071,-8]])
B2 = np.array([[0],[0],[4]])
C2 = np.array([[0.7071,-0.7071,0]])
D2 = np.array([[0]])

# Sistema 2 é dado por
sist_ss2 = ctrl.StateSpace(A2,B2,C2,D2)

# Transformando Espaço de Estado em FT e arredondando numerador
G2 = ctrl.ss2tf(sist_ss2)
G2 = arredondar(G2)
# Printando resposta letra (b)

print(f'(b)\n{G2}')

"""(c) Dessa forma, é facil ver que os espaços de estados são os mesmos, apenas multiplicados por alguma cte"""