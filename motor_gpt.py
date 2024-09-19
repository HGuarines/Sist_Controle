import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parâmetros do sistema
ttotal = 100
dt = 0.001
npassos = int(ttotal / dt)

ra = 0.01
la = 1.0
B = 1.0
J = 5.0
km = 1.0

# Inicialização das variáveis
ia = np.zeros(npassos)
omega = np.zeros(npassos)
va = np.full(npassos, 50.0)  # Inicializa va com 50.0 até 60s
Tm = np.full(npassos, 10.0)  # Inicializa Tm com 10.0 até 30s
t = np.arange(npassos) * dt

# Condições iniciais
ia[0] = 75.0
omega[0] = 0.0

# Atualização de va e Tm de acordo com o tempo
va[int(60.0 / dt):] = 0.0  # Após 60s, va = 0
Tm[int(30.0 / dt):] = 30.0  # Após 30s, Tm = 30

# Loop de integração
for i in range(npassos - 1):
    ia[i + 1] = ia[i] + (((va[i] - (km * omega[i])) / la) - ((ra / la) * ia[i])) * dt
    omega[i + 1] = omega[i] + ((((km * ia[i]) - Tm[i]) / J) - ((B / J) * omega[i])) * dt

# Plotando os resultados
# fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# ax[0].plot(t, ia, 'r', lw=2, label='Corrente de armadura')
# ax[0].set_xlabel('Tempo (s)')
# ax[0].set_ylabel('ia (A)')
# ax[0].grid(True)
# ax[0].legend()

# ax[1].plot(t, omega, 'g', lw=2, label='Velocidade do eixo')
# ax[1].set_xlabel('Tempo (s)')
# ax[1].set_ylabel('Velocidade (rad/s)')
# ax[1].grid(True)
# ax[1].legend()

# plt.tight_layout()
# plt.show()

# Criando o DataFrame para visualização
df = pd.DataFrame({
    'Tempo (s)': t,
    'Tensão de armadura (Va)': va,
    'Corrente de armadura (Ia)': ia,
    'Torque mecânico (Tm)': Tm,
    'Velocidade do eixo (Omega)': omega
})


# Exibindo as primeiras linhas do DataFrame
display(df.loc())

# Plotando usando o próprio Pandas
df.plot(x='Tempo (s)', subplots=True, figsize=(10, 8), grid=True)
plt.tight_layout()
plt.show()