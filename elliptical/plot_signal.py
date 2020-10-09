# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def getParent(path, levels=1): 
    for i in range(levels + 1): #pylint: disable=unused-variable
        parent = os.path.dirname(path)
        path = parent
    return os.path.abspath(path)
file = getParent(__file__)


freqs = [10,20,22,25,30]
y_ticks = np.linspace(-0.2,0.2,41)
fig, ax = plt.subplots()
for index,f in enumerate(freqs):
    # Importing the dataset
    dataset = pd.read_csv(f'{file}/csv_files/ellip{index+1}_signal.csv')
    time = dataset.iloc[:, 0].values
    vout = dataset.iloc[:, 1].values
    time = time*1e3
    ax.plot(time, vout, label=f'{f} kHz')



ax.set_title('Analise da saida')
ax.set_ylabel('Tensao (V)')
ax.set_xlabel('Tempo (ms)')
# ax.set_xlim(left=0, right=time[-1])
ax.grid(color='b', ls='-.', lw=0.25)
plt.yticks(y_ticks)
plt.legend(loc='upper right')
plt.show()
