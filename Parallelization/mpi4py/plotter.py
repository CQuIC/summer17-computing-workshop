import numpy as np
import json
import glob
import matplotlib.pyplot as plt

try:
    import seaborn
except Exception:
    print('Seaborn not installed on this machine.')

def make_plot():
    r'''Makes a plot of mean displacement of the random walk as a function
    of time

    Inputs
    ------
    None. Reads in json files from the simulated_data directory and processes them

    Outputs
    -------
    fig. A matplotlib figure showing the mean displacement for all the random walks
         contained in the simulated_data directory. Writes the figure to disk.
    '''

    #Grab all the data files
    files = glob.glob('simulated_data/*.json')
    data_holder = []

    for fi in files:
        with open(fi, 'r') as f:
            data = json.load(f)

        data_holder.append([data['p'], np.int_(data['trajectories'])])

    #Sort the list of (p, trajectory) values by p
    #(Makes the plot easier to comprehend)
    data_holder.sort()

    #Make a matplotlib figure
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    for element in data_holder:
        ax.plot(np.mean(element[1], axis=0), label=np.round(element[0], 2))

    ax.legend(loc=0, frameon=True, fancybox=True)
    ax.set_xlabel('Timestep', fontsize=20)
    ax.set_ylabel('Mean Displacement', fontsize=20)
    ax.set_title('Examining Behavior of a Random Walk', fontsize=25)
    fig.savefig('mean_trajectory.pdf', bbox_inches='tight')

    plt.close()

if __name__ == '__main__':
    print('Making plot.')
    make_plot()
    print('Plot complete!')