import numpy as np
import matplotlib.pyplot as plt

# Define os autovalores para a matriz A dada
def calc_autovalores(K):
    A = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [-2, -K, -2]])
    autovalores, _ = np.linalg.eig(A)
    return autovalores

# Range dos valores de K
K_values = np.linspace(0, 100, 500)

# Plot do gráfico
plt.figure(figsize=(10, 6))

# Computando e plotando os polos para cada valor de K
for K in K_values:
    autovalores = calc_autovalores(K)
    plt.plot(np.real(autovalores), np.imag(autovalores), 'bx')

plt.axvline(0, color='r', linestyle='--')  # Indicando o eixo imaginario
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Mapa dos Polos e Zeros para K (0 <= K <= 100)')
plt.grid(True)
plt.show()
