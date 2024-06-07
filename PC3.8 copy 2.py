import numpy as np
import matplotlib.pyplot as plt

# Definir a função para calcular os autovalores para um dado K
def calcular_autovalores(K):
    A = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [-2, -K, -2]
    ])
    autovalores = np.linalg.eigvals(A)
    return autovalores

# Intervalo de K
K_values = np.linspace(0, 100, 1000)

# Armazenar autovalores
autovalores_reais = []
autovalores_imaginarios = []

# Calcular autovalores para cada valor de K
for K in K_values:
    autovalores = calcular_autovalores(K)
    autovalores_reais.append(np.real(autovalores))
    autovalores_imaginarios.append(np.imag(autovalores))

# Converter para numpy arrays para facilitar a manipulação
autovalores_reais = np.array(autovalores_reais)
autovalores_imaginarios = np.array(autovalores_imaginarios)

# Plotar autovalores reais
plt.figure(figsize=(10, 5))
for i in range(autovalores_reais.shape[1]):
    plt.plot(K_values, autovalores_reais[:, i], label=f'Autovalor {i+1}')
plt.xlabel('K')
plt.ylabel('Parte Real dos Autovalores')
plt.title('Parte Real dos Autovalores em Função de K')
plt.legend()
plt.grid(True)
plt.show()

# Plotar autovalores imaginários
plt.figure(figsize=(10, 5))
for i in range(autovalores_imaginarios.shape[1]):
    plt.plot(K_values, autovalores_imaginarios[:, i], label=f'Autovalor {i+1}')
plt.xlabel('K')
plt.ylabel('Parte Imaginária dos Autovalores')
plt.title('Parte Imaginária dos Autovalores em Função de K')
plt.legend()
plt.grid(True)
plt.show()
