
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the simulation
alpha = 1.0  # Diffusion coefficient
kappa = 0.1  # Decoherence strength
epsilon = 1e-5  # Regularization for decoherence
dt = 0.01  # Time step
dx = 0.1  # Spatial step
L = 10  # Spatial domain size
N_x = int(2 * L / dx)  # Number of spatial points
N_t = 500  # Number of time steps
x = np.linspace(-L, L, N_x)  # Spatial grid
t = np.linspace(0, N_t * dt, N_t)  # Temporal grid

# Initialize the quantum state (Gaussian initial condition)
G = np.zeros((N_x, N_t))
G[:, 0] = np.exp(-((x - 2) ** 2) / (2 * 1.0 ** 2))  # Initial Gaussian

# Noise model for real-world conditions
def noise_model(G, noise_amplitude=0.05):
    noise = np.random.normal(0, noise_amplitude, G.shape)
    return G + noise

# Simulating quantum state evolution with noise
for n in range(1, N_t):
    # Compute the diffusion term
    laplacian = (np.roll(G[:, n - 1], -1) - 2 * G[:, n - 1] + np.roll(G[:, n - 1], 1)) / dx**2
    # Apply noise model
    noisy_G = noise_model(G[:, n - 1])
    # Update the quantum state with diffusion and decoherence
    G[:, n] = G[:, n - 1] + dt * (
        alpha * laplacian
        - kappa * (G[:, n - 1] ** 2 / (1 + G[:, n - 1] ** 2) + epsilon)
    )

# Visualizing simulation results
plt.figure(figsize=(12, 6))
plt.contourf(t, x, G, levels=100, cmap="viridis")
plt.colorbar(label="Quantum State G(x, t)")
plt.title("Multi-Particle Chain Simulation with Noise")
plt.xlabel("Time (t)")
plt.ylabel("Space (x)")
plt.show()
