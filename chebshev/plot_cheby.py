from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import sympy

Fn = 22e3
fc = 2*np.pi*Fn
ordem = np.arange(2,9)

for N in ordem:
    b, a = signal.cheby1(N, 0.5, fc, 'low', analog=True)
    w, h = signal.freqs(b, a)
    plt.semilogx(w/(2*np.pi), 20 * np.log10(abs(h)), label=f'Ordem = {N}')

yticks = np.arange(0,-80,-10)
plt.title('Resposta em frequência do filtro Chebyshev')
plt.xlabel('Frequencia [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(Fn, color='green')  # cutoff frequency
plt.legend(loc='upper right')
plt.yticks(yticks)
plt.show()
