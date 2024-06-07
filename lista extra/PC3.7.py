""" Resolução da questão PC3.7 """

import control.matlab as ctrl # lsim só funciona no .matlab
import numpy as np
import matplotlib.pyplot as plt

# Definindo as matrizes do Espaço de Estado
A = np.array([[0,1],[-2,-3]])
B = np.array([[0],[1]])
C = np.array([[1,0]])
D = np.array([[0]])

# Definindo as condições iniciais
x0 = np.array([[1],[0]])

# Criando sistema EE
sist_ss = ctrl.StateSpace(A, B, C, D)

# Definindo variaveis 
u = 0
t = np.linspace(0, 10, 500)

# Calculando a resposta do sistema
y_out, T_out, x_out = ctrl.lsim(sist_ss,u,t,x0)

# Plotando gráfico da respsota

plt.figure()
plt.plot(T_out, x_out)
plt.xlabel('$Tempo (s)$')
plt.ylabel('$Saidas X(t)$')
plt.title('Respostas Naturais do Sistema')
plt.grid(True)
plt.legend(['$X_1 (t)$', '$X_2 (t)$'])
plt.show()