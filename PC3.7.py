import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lsim, StateSpace

# Definir as matrizes do sistema
A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Condição inicial
x0 = np.array([1, 0])

# Definir o vetor de tempo
t = np.linspace(0, 10, 1000)

# Sinal de entrada (u(t) = 0)
u = np.zeros_like(t)

# Criar o sistema em espaço de estados
sistema = StateSpace(A, B, C, D)

# Simular a resposta do sistema
t, y, x = lsim(sistema, U=u, T=t, X0=x0)

# Plotar os resultados
plt.figure(figsize=(10, 6))
plt.plot(t, x[:, 0], label='$x_1(t)$')
plt.plot(t, x[:, 1], label='$x_2(t)$')
plt.title('Resposta do Sistema')
plt.xlabel('Tempo (segundos)')
plt.ylabel('Estados')
plt.legend()
plt.grid()
plt.show()
