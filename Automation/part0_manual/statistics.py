import qutip
import numpy as np
import pickle as pkl
import os

# Navigate to the directory containing the output of all the programs
os.chdir('output')

# Open the file containing the results of the simulation
inputfile = open('simulation/psi_t.pkl', 'rb')

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

# Create statistics output directory
if not os.path.isdir('statistics'):
    os.mkdir('statistics')

# Move to the statistics output directory
os.chdir('statistics')

# Open output file for saving the expectation values
outputfile_sigmax = open('exp_sigmax.pkl', 'wb')
outputfile_sigmay = open('exp_sigmay.pkl', 'wb')
outputfile_sigmaz = open('exp_sigmaz.pkl', 'wb')

# Save to output file
pkl.dump(exp_sigmax, file=outputfile_sigmax)
pkl.dump(exp_sigmay, file=outputfile_sigmay)
pkl.dump(exp_sigmaz, file=outputfile_sigmaz)

# Close output file
outputfile_sigmax.close()
outputfile_sigmay.close()
outputfile_sigmaz.close()

