import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

# Criando Função para arredondar os valores
def arredondar(ft):
    ft.num = [[ft.num[0][0].round(4)]]
    return ft

# Definindo as matrizes do espaço de estado
A = np.array([[0,1,0],[0,0,1],[-3,-2,-5]])
B = np.array([[0],[0],[1]])
C = np.array([[1,0,0]])
D = np.array([[0]])

# Definindo o espaço de estado
sist_ss = ctrl.StateSpace(A, B, C, D)

# Definindo a FT
G = ctrl.ss2tf(sist_ss)

# Corrigindo erros computacionais
G = arredondar(G)

# printando FT
print(f"(a) \n{G}")

# Definindo x0
x0 = np.array([0, -1, 1])

# Dado que é pedido t entre 0 e 10
t = np.linspace(0, 10, 500)

# # Teremos que a resposta inicial será
resposta_t, resposta_y, resposta_x = ctrl.initial_response(sist_ss, t, x0, return_x=True)

# Plotando 
plt.figure()
plt.plot(resposta_t, resposta_x[0], label='$x_1(t)$')
plt.plot(resposta_t, resposta_x[1], label='$x_2(t)$')
plt.plot(resposta_t, resposta_x[2], label='$x_3(t)$')
plt.xlabel('Tempo (s)')
plt.ylabel('$x(t)$')
plt.title('(b) Resposta do Sistema para a Condição Inicial $x(0)=[0, -1, 1]^T$')
plt.legend()
plt.grid(True)
plt.show()

# Calculando a matriz de transição de estados (phi) para t = 10
phi_t10 = expm(A * t[-1])

# calculando x(t) para t = 10
x_t10 = np.dot(phi_t10, x0)

# Respondendo letra C
print(f'(c)\nMatriz de transição: \n{phi_t10}\n')
print(f'Condição inicial para t = 0 \n{x0}\n')
print(f'Condição inicial para t = 10 \n{x_t10}')
