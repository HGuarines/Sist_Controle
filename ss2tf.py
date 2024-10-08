import control as ctrl
import numpy as np
import pandas as pd

# Definindo função para arredondar se não da merda ss matriz 3x3
def arredondar(FT):
    FT.num = [[FT.num[0][0].round(3)]]
    return FT


# Definindo as matrizes fornecidas
A = np.array([[0, 1, 0],
              [0, 0, 1],
              [-4, -5, -8]])
B = np.array([[0],
              [0],
              [4]])
C = np.array([[1, 0, 0]])
D = np.array([[0]])

# Criando o sistema de espaço de estados
sistema_ss = ctrl.StateSpace(A, B, C, D)

# Convertendo para função de transferência
G = arredondar(ctrl.ss2tf(sistema_ss))
# Imprimindo a função de transferência
# print(f"Função de Transferência: \n{G}")
display(G)

# Parei pra brincar com pandas e plotei o impulso
tempo = np.linspace(0, 10, 500)
_ , resp_i = ctrl.impulse_response(sistema_ss, tempo)


df = pd.DataFrame()

df.index = tempo
df.index.name = 'Tempo'
df['resposta_impulso'] = resp_i
df.plot();
print(df)
display(df)