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
valores_K = np.linspace(0, 100, 500)

# Lista para armazenar valores de K com algum autovalor no semiplano direito
valores_K_semiplano_esquerdo = []

# Plot do gráfico
plt.figure(figsize=(10, 6))

# Computando e plotando os polos para cada valor de K
for K in valores_K:
    autovalores = calc_autovalores(K)
    # Verifica se algum autovalor tem parte real negativa
    if np.all(np.real(autovalores) < 0):
        valores_K_semiplano_esquerdo.append(K)
    plt.plot(np.real(autovalores), np.imag(autovalores), 'bx')

valores_K_semiplano_esquerdo = np.round(valores_K_semiplano_esquerdo, 3)

# Imprime a lista de valores de K no semiplano direito após o loop
print("Valores de K com algum autovalor no semiplano direito:\n", valores_K_semiplano_esquerdo)

plt.axvline(0, color='r', linestyle='--')  # Indicando o eixo imaginário
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Mapa dos Polos e Zeros para K (0 <= K <= 100)')
plt.grid(True)
plt.show()
