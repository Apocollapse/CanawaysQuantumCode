
# Example Configuration for Phase Collapse
from cqc_simulator import CQC

# Define parameters
params = {
    "alpha": 0.01,
    "beta": 0.5,
    "gamma": 0.3,
    "nu": 0.2,
    "kappa": 0.5,
    "epsilon": 0.1,
    "time_steps": 500,
    "dt": 0.01,
    "x": np.linspace(-5, 5, 100),
    "boundary_condition": "reflective"
}

# Initialize wavefunction
G_initial = np.exp(-0.5 * params["x"]**2)

# Run simulation
cqc = CQC(params)
results = cqc.simulate(G_initial)
cqc.plot_results(results)
