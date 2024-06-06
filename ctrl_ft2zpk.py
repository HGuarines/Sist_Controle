""" Encontrar Zeros, Polos e Ganho dado Função de Transferencia"""

import control as ctrl
import scipy.signal as signal

# Definindo denominador e numerador:
num = [5, 10, 0]
den = [1, 5, 11, 5]

# Função de transferencia:
ft = ctrl.TransferFunction(num, den)

# Encontrando Zeros, polos e ganho
zeros, polos, ganho = signal.tf2zpk(num, den)

print("Zeros:", zeros)
print("Polos:", polos)
print("Ganho:", ganho)
