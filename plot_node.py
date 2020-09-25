from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

Q = np.array([0.1, 0.5, 0.707,1, 2, 10])

for i in Q:
    s1 = signal.lti([1.5791367e+10],
                    [1.00000000e+00, 1.77715318e+05/i, 1.57913670e+10])
    w, mag, phase = s1.bode()
    plt.semilogx(w/(2*np.pi), mag, label=f'Q = {i}')    # Bode magnitude plot

plt.xlabel('Frequencia [Hz]')
plt.ylabel('Magnitude [dB]')
plt.xlim(1e2, 1e5)
plt.legend(loc='upper right')
plt.grid(which='both', axis='both')
plt.show()
