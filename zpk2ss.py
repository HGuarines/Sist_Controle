""" Descobrindo o ss (space state) a partir de zpk"""

import control as ctrl
import scipy.signal as signal

zero = [-1]
polo = [-3, -5]
ganho = [10]

num, den = signal.zpk2tf(zero, polo, ganho)

# Criando a função de transferência
G = ctrl.TransferFunction(num, den)
print(f"Função de Transferência: {G}")

# Convertendo para Estado de Espaço
sistema_ss = ctrl.tf2ss(G)

# Exibindo as matrizes de estado
print("\nRepresentação em Espaço de Estados:")
print(f"Matriz A:\n{sistema_ss.A}")
print(f"Matriz B:\n{sistema_ss.B}")
print(f"Matriz C:\n{sistema_ss.C}")
print(f"Matriz D:\n{sistema_ss.D}")
