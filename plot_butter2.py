from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('./bode_filtro.csv')
freq = dataset.iloc[:, 0].values
mag = dataset.iloc[:, 1].values

Fn = 22e3
fc = 2*np.pi*Fn
ordem = [8]

# Grafico 1
plt.semilogx(freq, mag, label='Filtro implementado')
# Grafico2
for N in ordem:
    b, a = signal.butter(N, fc, 'low', analog=True)
    w, h = signal.freqs(b, a)
    plt.semilogx(w/(2*np.pi), 20 * np.log10(abs(h)), label=f'Filtro ideal')


yticks = np.arange(0,-80,-10)
plt.title('Resposta em frequência do filtro butterworth')
plt.xlabel('Frequencia [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(Fn, color='green')  # cutoff frequency
plt.legend(loc='upper right')
plt.yticks(yticks)
plt.ylim(-70,10)
plt.show()
