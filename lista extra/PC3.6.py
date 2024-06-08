""" Resolução da questão PC3.6"""

import control as ctrl
import matplotlib.pyplot as plt
# Definindo numerador e denominador da FT do controlador
numc = [3]
denc = [1,3]

# FT do controlador
Gc = ctrl.TransferFunction(numc, denc)

# Transformando em variaveis de estado
sist_ssc = ctrl.tf2ss(Gc)

# Resposta (a)
print('(a)\nRepresentação do controlador em espaços de estados')
print(f'A = {sist_ssc.A}')
print(f'B = {sist_ssc.B}')
print(f'C = {sist_ssc.C}')
print(f'D = {sist_ssc.D}')

# Definindo numerador e denominador da FT do processo
nump = [1]
denp = [1,2,5]

# Ft do processo
Gp = ctrl.TransferFunction(nump, denp)

# Transformando em variaveis de estado
sist_ssp = ctrl.tf2ss(Gp)

# Resposta (b)
print('\n(b)\nRepresentação do processo em espaços de estados')
print(f'A = \n{sist_ssp.A}')
print(f'B = \n{sist_ssp.B}')
print(f'C = \n{sist_ssp.C}')
print(f'D = \n{sist_ssp.D}')

# Multiplicando controlador por processo
sist_serie = ctrl.series(Gc, Gp)

# Fazendo a realimentação negativa (feedback ja assume negativa)
sist_realiment = ctrl.feedback(sist_serie)

# Transformando em variaveis de estado
sist_sstotal = ctrl.tf2ss(sist_realiment)

# calculando o impulso
t, impulso = ctrl.impulse_response(sist_sstotal)

# (c)
plt.figure()
plt.plot(t, impulso)
plt.xlabel('$Tempo (s)$')
plt.ylabel('$Amplitude$')
plt.title('(c) Resposta do sistema em malha fechada ao impulso')
plt.grid(True)
plt.show()