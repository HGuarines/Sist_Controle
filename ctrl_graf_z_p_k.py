""" Plotar degrau dado zeros, polos e ganho """

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import scipy.signal as signal

# Definindo zeros, polos e ganho
zeros = [0, -2]
polos = [-3, -1 + 2j, -1 - 2j]
ganho = 5

# Utilizando zpk para criar a função de transferência se possível
# Convertendo zeros, polos e ganho para numerador e denominador
num, den = signal.zpk2tf(zeros, polos, ganho)

# Criando a função de transferência
ft = ctrl.TransferFunction(num, den)

# Definindo o vetor de tempo para a simulação da resposta ao degrau
tempo = np.linspace(0, 10, 500)

# Calculando a resposta ao degrau
tempo_d, resposta_d = ctrl.step_response(ft, tempo)

# Plotando a resposta ao degrau
plt.figure(figsize=(10, 6))
plt.plot(tempo_d, resposta_d)
plt.title('Resposta ao Degrau')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
