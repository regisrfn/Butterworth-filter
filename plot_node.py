from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

Fn = 22e3
Wc = np.sqrt(1.91075541e+10)
Q = np.array([0.3, 0.5, 0.707, 1, 2, 10])

for i in Q:
    s1 = signal.lti([1.91075541e+10],
                    [1.00000000e+00, Wc/i, 1.91075541e+10])
    w, mag, phase = s1.bode()
    # Bode magnitude plot
    plt.semilogx(w/(2*np.pi), mag, label=f'Q = {i}')

plt.scatter(Fn, -3)
plt.xlabel('Frequencia [Hz]')
plt.ylabel('Magnitude [dB]')
plt.legend(loc='upper right')
plt.grid(which='both', axis='both')
plt.axvline(Fn, color='green')  # cutoff frequency
plt.show()
