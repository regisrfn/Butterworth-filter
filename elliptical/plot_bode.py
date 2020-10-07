from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def getParent(path, levels=1):
    for i in range(levels + 1): #pylint: disable=unused-variable
        parent = os.path.dirname(path)
        path = parent
    return os.path.abspath(path)
file = getParent(__file__)

# Importing the dataset
dataset = pd.read_csv(f'{file}/csv_files/bode_ellip.csv')
freq = dataset.iloc[:, 0].values
mag = dataset.iloc[:, 1].values

Fn = 22e3
fc = 2*np.pi*Fn
ordem = [6]
rp = 0.5
rs = 33

# Grafico 1
plt.semilogx(freq, mag, label='Filtro implementado')
# Grafico2
for N in ordem:
    b, a = signal.ellip(N, rp, rs, fc, 'low', analog=True)
    w, h = signal.freqs(b, a)
    plt.semilogx(w/(2*np.pi), 20 * np.log10(abs(h)), label=f'Filtro ideal')


plt.title('Resposta em frequência do filtro Eliptico')
plt.xlabel('Frequencia [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(Fn, color='green')  # cutoff frequency
plt.axhline(-0.5, color='green') # ripple
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
