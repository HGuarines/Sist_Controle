""" Resposta ao Impulso do Sistema em Malha Fechada a partir das FT"""

import control as ctrl
import matplotlib.pyplot as plt

# Definindo as funções de transferência do controlador e do processo
FT_controlador = ctrl.TransferFunction([3], [1, 3])
FT_processo = ctrl.TransferFunction([1], [1, 2, 5])

# Combinando controlador e processo em série
sist_serie = ctrl.series(FT_controlador, FT_processo)

# Obtendo sistema em malha fechada
sist_malha_fechada = ctrl.feedback(sist_serie, 1)

# Convertendo sistema em malha fechada para a representação em espaço de estados
sistema_ss = ctrl.tf2ss(sist_malha_fechada)

# Obter a resposta ao impulso do sistema em malha fechada
t, y = ctrl.impulse_response(sistema_ss)

# Plotar a resposta ao impulso
plt.figure()
plt.plot(t, y)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Resposta ao Impulso do Sistema em Malha Fechada')
plt.grid(True)
plt.show()
