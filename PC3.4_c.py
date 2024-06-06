import numpy as np
from scipy.linalg import expm

# Definindo as matrizes do sistema no espaço de estados
A = np.array([[0, 1, 0],
              [0, 0, 1],
              [-3, -2, -5]])
x0 = np.array([0, -1, 1])

# Tempo para o qual queremos calcular x(t)
t_10 = 10

# Calculando a matriz de transição de estado em t = 10
phi_t10 = expm(A * t_10)  # Calculando e^(At)

# Calculando x(t) em t = 10
# Multiplicando a matriz de transição pelo vetor de condição inicial
x_t10 = np.dot(phi_t10, x0)

# Imprimindo os resultados
print(f"Matriz de transição de estado (phi(t)) em t = {t_10}:\n{phi_t10}")
print(f"Estado x(t) em t = {
      t_10} para a condição inicial x(0) = {x0}:\n{x_t10}")
