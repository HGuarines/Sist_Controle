# Primeiro importa-se as bibliotecas
# Note que 'as np' e outros seria um tipo de apelido para o comando

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Numerador e denominador da FT G(s) = s + 3 / s^2 + 2s + 3
num = [1, 3]
den = [1, 2, 3]

# Criando o sistema
sistema = ctrl.TransferFunction(num, den)

# Analise do degrau (que seria uma força cte)

# Como a analise é do degrau, é necessário escolher um tempo de simulação
# Nesse caso no numpy.linspace() os valores inseidos são, respectivamente:
# O valor inicial do tempo, o valor final e a quantidade de pontos calculados
tempo = np.linspace(0, 10, 100)

# Resposta ao degrau
degrau_t, degrau_r = ctrl.step_response(sistema, T=tempo)

# Resposta ao impulso
impulso_t, impulso_r = ctrl.impulse_response(sistema, T=tempo)

# Plotando a resposta

# plt.figure(figsize=(10, 6))
# plt.plot(degrau_t, degrau_r, label='Resposta ao Degrau')
# plt.plot(impulso_t, impulso_r, label='Resposta ao impulso')
# plt.title('Resposta no tempo')
# plt.xlabel('Tempo (s)')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.grid(True)
# plt.show()

df = pd.DataFrame()

df.index = tempo
df['resposta_degrau'] = degrau_r
df['resposta_impulso'] = impulso_r
df.plot(grid=True);