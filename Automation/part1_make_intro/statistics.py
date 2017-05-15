import qutip
import numpy as np
import pickle as pkl
import os

# Open the file containing the results of the simulation
inputfile = open('psi_t.pkl', 'rb')

# Read the state vector at different tims
psi_t = pkl.load(inputfile)

# Close the input file
inputfile.close()


# Using functionality of the qutip library, we compute expectation
# values of sigmax, sigmay and sigmaz
exp_sigmax = qutip.expect(qutip.sigmax(), psi_t.states)
exp_sigmay = qutip.expect(qutip.sigmay(), psi_t.states)
exp_sigmaz = qutip.expect(qutip.sigmaz(), psi_t.states)

# Now, we will save the expectation values to files

# Open output file for saving the expectation values
outputfile_sigma = open('exp_sigma.pkl', 'wb')

# Save to output file
pkl.dump((exp_sigmax, exp_sigmay, exp_sigmaz), file=outputfile_sigma)

# Close output file
outputfile_sigma.close()

