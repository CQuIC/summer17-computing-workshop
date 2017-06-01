from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

np.random.seed(0)

p = np.random.uniform(0, 1)

print('Hello from {0}. I have value {1}'.format(rank, p))