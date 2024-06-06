import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Definindo as matrizes do sistema no espaço de estados
A = np.array([[0, 1, 0],
              [0, 0, 1],
              [-3, -2, -5]])
B = np.array([[0],
              [0],
              [1]])
C = np.array([[1, 0, 0]])
D = np.array([[0]])

# Criando o sistema de espaço de estados
sistema_ss = ctrl.StateSpace(A, B, C, D)

# Definindo a condição inicial
x0 = [0, -1, 1]

# Simulando a resposta do sistema com condição inicial
t = np.linspace(0, 10, 1000)  # 0 a 10 segundos, com 1000 pontos no tempo
t_response, y_response, x_response = ctrl.initial_response(
    sistema_ss, t, x0, return_x=True)

# Plotando a resposta do sistema
plt.figure()
plt.plot(t_response, x_response[0], label='$x_1(t)$', color='b')  # Azul
plt.plot(t_response, x_response[1], label='$x_2(t)$', color='g')  # Verde
plt.plot(t_response, x_response[2], label='$x_3(t)$', color='r')  # Vermelho
plt.xlabel('Tempo (s)')
plt.ylabel('$x(t)$')
plt.title('Resposta do Sistema para a Condição Inicial $x(0)=[0, -1, 1]^T$')
plt.legend()
plt.grid(True)
plt.show()
