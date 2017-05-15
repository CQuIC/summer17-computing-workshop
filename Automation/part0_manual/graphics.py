import qutip
import numpy as np
import pickle as pkl
import os
import matplotlib.pyplot as plt

# Navigate to the directory containing the output of all the programs
os.chdir('output')

# Open the files containing the expectation values
inputfile_sigmax = open('statistics/exp_sigmax.pkl', 'rb')
inputfile_sigmay = open('statistics/exp_sigmay.pkl', 'rb')
inputfile_sigmaz = open('statistics/exp_sigmaz.pkl', 'rb')

# Read the state vector at different tims
exp_sigmax = pkl.load(inputfile_sigmax)
exp_sigmay = pkl.load(inputfile_sigmay)
exp_sigmaz = pkl.load(inputfile_sigmaz)

# Close the input file
inputfile_sigmax.close()
inputfile_sigmay.close()
inputfile_sigmaz.close()

# Open the file containing the results of the simulation
inputfile = open('simulation/psi_t.pkl', 'rb')

# Read the state vector at different tims
psi_t = pkl.load(inputfile)

# Close the input file
inputfile.close()

# Next we read the time steps

# Open the file containing the time steps
inputfile_tsteps = open('tsteps.pkl', 'rb')

# Read the time steps
tsteps = pkl.load(inputfile_tsteps)

# Close the file containing the time steps
inputfile_tsteps.close()

# Now to the actual graphics.

# Create the directory for storing graphics
if not os.path.isdir('graphics'):
    os.mkdir('graphics')

# Move to the directory for storing graphics
os.chdir('graphics')

# First we plot the expectation values of
# sigmax, sigmay and sigmaz
plt.plot(tsteps, exp_sigmax, color='b', label='$\\langle\\sigma_x\\rangle$')
plt.plot(tsteps, exp_sigmay, color='r', label='$\\langle\\sigma_y\\rangle$')
plt.plot(tsteps, exp_sigmaz, color='g', label='$\\langle\\sigma_z\\rangle$')         

# Make some space
plt.ylim(-1, 1)

# Show the legend, add axis titles
plt.xlabel('Time, $t / \\frac{1}{\\omega}$')
plt.ylabel('Expecation value of $\\sigma$, $\\langle\\sigma\\rangle / \\frac{\hbar}{2}$')
plt.legend(loc='best')

# Save the plot
plt.savefig('exp_sigma.eps', filetype='eps')
plt.close()

# Next we plot four steps in the rotation of the Bloch vector
# using the functionality provided by the qutip library

n_tsteps_one_oscillation = 32
n_tsteps_skip = 8
sphere = qutip.Bloch()
sphere.sphere_alpha = 0.0
sphere.vector_color = ['b','r','g','#CC6600']

# Mark the initial Bloch vector for reference
a_0 = [exp_sigmax[0], exp_sigmay[0], exp_sigmaz[0]]
sphere.add_points(a_0)


sphere.add_states(psi_t.states[:n_tsteps_one_oscillation][::n_tsteps_skip])
sphere.make_sphere()
sphere.render()
plt.savefig('bloch.eps', filetype='eps')
