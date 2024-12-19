
import numpy as np

def hadamard_gate(qubit):
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    qubit_rotated = np.dot(H, qubit[:2])
    return np.append(qubit_rotated, qubit[2])

def cnot_gate(control, target):
    if control[2] > 0:
        target[0], target[1] = -target[0], -target[1]
    return control, target

def simulate_cqc(timesteps, dt, kappa, initial_states):
    qubit_1, qubit_2 = initial_states
    results = []
    for t in range(timesteps):
        qubit_1 *= (1 - kappa * dt)
        qubit_2 *= (1 - kappa * dt)
        if t == int(10 / dt):
            qubit_1 = hadamard_gate(qubit_1)
        if t == int(20 / dt):
            qubit_1, qubit_2 = cnot_gate(qubit_1, qubit_2)
        results.append((qubit_1.copy(), qubit_2.copy()))
    return results
