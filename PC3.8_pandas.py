""" Resolução da questão PC3.8 """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define os autovalores para a matriz A dada
def calc_autovalores(K):
    A = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [-2, -K, -2]])
    autovalores, _ = np.linalg.eig(A)
    return autovalores

# Faixa dos valores de K
valores_K = np.linspace(0, 100, 500)

# Cria um DataFrame para armazenar os autovalores e o valor correspondente de K
df = pd.DataFrame({
    'K': valores_K,
    'autovalores': [calc_autovalores(K) for K in valores_K]
})

# Adiciona colunas separando as partes reais e imaginárias dos autovalores
df['parte_real_1'] = df['autovalores'].apply(lambda x: np.real(x[0]))
df['parte_real_2'] = df['autovalores'].apply(lambda x: np.real(x[1]))
df['parte_real_3'] = df['autovalores'].apply(lambda x: np.real(x[2]))

df['parte_imag_1'] = df['autovalores'].apply(lambda x: np.imag(x[0]))
df['parte_imag_2'] = df['autovalores'].apply(lambda x: np.imag(x[1]))
df['parte_imag_3'] = df['autovalores'].apply(lambda x: np.imag(x[2]))

# Verifica se todos os autovalores têm a parte real negativa (semiplano esquerdo)
df['todos_no_semiplano_esquerdo'] = (df[['parte_real_1', 'parte_real_2', 'parte_real_3']] < 0).all(axis=1)

# Filtra os valores de K onde todos os autovalores estão no semiplano esquerdo
faixa_k_semiplano_esquerdo = df[df['todos_no_semiplano_esquerdo']]['K']

# Exibir a faixa de K no console
if not faixa_k_semiplano_esquerdo.empty:
    print(f'Faixa de K onde todos os autovalores estão no semiplano esquerdo: {faixa_k_semiplano_esquerdo.min():.2f} <= K <= {faixa_k_semiplano_esquerdo.max():.2f}')
else:
    print('Não há valores de K onde todos os autovalores estão no semiplano esquerdo.')

# Plot do gráfico
plt.figure(figsize=(10, 6))

# Plotando os autovalores no gráfico (parte real e imaginária)
plt.plot(df['parte_real_1'], df['parte_imag_1'], 'bx', label='Autovalor 1')
plt.plot(df['parte_real_2'], df['parte_imag_2'], 'gx', label='Autovalor 2')
plt.plot(df['parte_real_3'], df['parte_imag_3'], 'rx', label='Autovalor 3')

# Exibir a linha do eixo imaginário no gráfico
plt.axvline(0, color='r', linestyle='--')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Mapa dos Polos e Zeros para K (0 <= K <= 100)')
plt.legend()
plt.grid(True)
plt.show()
