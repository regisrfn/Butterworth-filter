# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def getParent(path, levels=1):
    for i in range(levels + 1):
        parent = os.path.dirname(path)
        path = parent
    return os.path.abspath(path)
file = getParent(__file__)

# Importing the dataset
dataset = pd.read_csv(f'{file}/csv_files/filtro_cheby.csv')
time = dataset.iloc[:, 0].values
vout = dataset.iloc[:, 1].values
vent = dataset.iloc[:, 2].values


time = time*1e3

y_ticks = np.linspace(-5,5,21)
fig, ax = plt.subplots()
ax.set_title('Analise da saida')
ax.set_ylabel('Tensao (V)')
ax.set_xlabel('Tempo (ms)')
# ax.set_xlim(left=0, right=time[-1])
ax.grid(color='b', ls='-.', lw=0.25)
ax.plot(time, vent, label='sinal original')
ax.plot(time, vout, label='sinal filtrado')
plt.legend(loc='upper right')
plt.show()
