from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

Fn = 22e3
fc = 2*np.pi*Fn
N = 2

b, a = signal.butter(N, fc, 'low', analog=True)
w, h = signal.freqs(b, a)


plt.semilogx(w/(2*np.pi), 20 * np.log10(abs(h)), label=f'Ordem = {N}')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(Fn, color='green')  # cutoff frequency
plt.legend(loc='upper right')
plt.show()

Wc_square = a[2]
Wc = np.sqrt(a[2])
Q = Wc/a[1]
K = 3.0 - 1/Q
C = 1E-9
R = 1/(Wc*C)
R3 = 10E3
R4 = R3*(K-1)

print(f'R1 = {R}')
print(f'R3 = {R3}')
print(f'R4 = {R4}')
print(f'C2 = {C}')
print(f'Wc = {Wc}')
print(f'Q = {Q}')
print(f'K = {K}')
print(f'Eq = {a}')