import numpy as np
import matplotlib.pyplot as plt

# Define the state-space matrices
def get_eigenvalues(K):
    A = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [-2, -K, -2]])
    eigenvalues, _ = np.linalg.eig(A)
    return eigenvalues

# Range of K values
K_values = np.linspace(0, 100, 500)

# Plot setup
plt.figure(figsize=(10, 6))

# Compute and plot poles for each K
for K in K_values:
    eigenvalues = get_eigenvalues(K)
    plt.plot(np.real(eigenvalues), np.imag(eigenvalues), 'bx')

plt.axvline(0, color='r', linestyle='--')  # Indicate the imaginary axis
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Pole-Zero Map for varying K (0 <= K <= 100)')
plt.grid(True)
plt.show()
