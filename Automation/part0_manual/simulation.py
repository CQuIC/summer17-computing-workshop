import qutip
import numpy as np
import pickle as pkl
import os

# Hamiltonian
H = -qutip.sigmaz()

# Number of oscillations
n_oscillations = 4

# Number of time steps at which to store results
n_tsteps = 128

# List of times for which the solver should store the state vector
tsteps = np.linspace(0, n_oscillations*np.pi, n_tsteps)

# Get a random pure qubit state, parameterized by
# the polar angle theta of the Bloch vector and the
# azimuthal angle phi of the Bloch vector
np.random.seed(1)
theta = np.random.uniform(low=0, high=np.pi)
phi = np.random.uniform(low=0, high=2*np.pi)

# The state is defined using the qutip library's
# basis states for qubits
psi_0 = np.cos(theta/2) * qutip.basis(2, 0) + np.exp(1j*phi)*np.sin(theta/2) * qutip.basis(2, 1)

# Solve for the state vector at different times
# using the qutip library.
psi_t = qutip.mesolve(H, psi_0, tsteps, [], [])

# Now, we will save the output to a file

# Create simulation output directory
if not os.path.isdir('output'):
    os.mkdir('output')

# Navigate to the location where to store output
os.chdir('output')

# First we will save parameters of the simulation

# Open output file for saving the Hamiltonian
outputfile = open('hamiltonian.pkl', 'wb')

# Save to output file
pkl.dump(H, file=outputfile)

# Close output file
outputfile.close()

# Open output file for saving the time steps
outputfile = open('tsteps.pkl', 'wb')

# Save to output file
pkl.dump(tsteps, file=outputfile)

# Close output file
outputfile.close()


# Create simulation output directory
if not os.path.isdir('simulation'):
    os.mkdir('simulation')

# Move to simulation output directory
os.chdir('simulation')

# Open output file for saving the state vector
outputfile = open('psi_t.pkl', 'wb')

# Save to output file
pkl.dump(psi_t, file=outputfile)

# Close output file
outputfile.close()
