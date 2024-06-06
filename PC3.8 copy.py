import numpy as np
import matplotlib.pyplot as plt

# Função para calcular autovalores


def calcular_autovalores(K):
    # Definir a matriz de estado A com o valor de K variável
    A = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [-2, -K, -2]])
    # Calcular os autovalores da matriz A
    autovalores = np.linalg.eigvals(A)
    return autovalores


# Gerar intervalo de valores para K
K_values = np.linspace(-100, 100, 500)

# Calcular autovalores para cada valor de K
autovalores = np.array([calcular_autovalores(K) for K in K_values])

# Plotar os autovalores
plt.figure(figsize=(10, 6))
for i in range(3):  # Iterar sobre cada um dos três autovalores
    plt.plot(K_values, autovalores[:, i].real,
             label=f'Autovalor {i+1} (parte real)')
    plt.plot(K_values, autovalores[:, i].imag, linestyle='dashed', label=f'Autovalor {
             i+1} (parte imaginária)')

# Adicionar linha horizontal em y=0 para referência
plt.axhline(0, color='black', linewidth=0.5)
# Adicionar rótulos aos eixos x e y, título e legenda ao gráfico
plt.xlabel('K')
plt.ylabel('Autovalores')
plt.title('Autovalores em função de K')
plt.legend()
plt.grid(True)
plt.show()

# Determinar o intervalo de K para autovalores no semiplano esquerdo
K_estavel = []
for K in K_values:
    autovalores_atual = calcular_autovalores(K)
    # Verificar se todas as partes reais são negativas
    if np.all(np.real(autovalores_atual) < 0):
        K_estavel.append(K)

# Imprimir intervalo de K para estabilidade
print(f'Intervalo de K para estabilidade: {K_estavel[0]} a {K_estavel[-1]}')
