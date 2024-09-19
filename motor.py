import numpy as np
import matplotlib.pyplot as plt

ttotal = 100
dt = 0.001
npassos = int(ttotal/dt)

ra = 0.01
la = 1.0
B = 1.0
J = 5.0
km = 1.0

ia = np.zeros(npassos)
omega = np.zeros(npassos)
va = np.zeros(npassos)
Tm = np.zeros(npassos)
t = np.arange(npassos)*dt

ia[0] = 75.0
omega[0] = 0.0
va[0] = 50.0
Tm[0] = 10.0

for i in range(npassos-1):

  if i <= (60.0/dt):
    va[i] = 50.0
  if i > (60.0/dt):
    va[i] = 0.0

  if i <= (30/dt):
    Tm[i] = 10
  if i > (30/dt):
    Tm[i] = 30

  ia[i+1] = ia[i] + (((va[i] - (km*omega[i]))/la) - ((ra/la)*ia[i]))*dt
  omega[i+1] = omega[i] + ((((km*ia[i]) - Tm[i])/J) - ((B/J)*omega[i]))*dt

plt.figure(figsize=[20, 4])
fig = plt.figure(1); fig.clf()
plt.plot(t, ia,'r', lw=3, label='Corrente de armadura')
fig.legend(); plt.xlabel('tempo'); plt.ylabel('ia'); plt.grid()

plt.figure(figsize=[20, 4])
fig = plt.figure(2); fig.clf()
plt.plot(t, omega,'g', lw=3, label='Velocidade do eixo')
fig.legend(); plt.xlabel('tempo'); plt.ylabel('Ômega'); plt.grid()