from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import sympy

Fn = 22e3
fc = 2*np.pi*Fn
N = 4

b, a = signal.butter(N, fc, 'low', analog=True)
z, p, k = signal.butter(N, fc, 'low', analog=True,output='zpk')
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

a = np.poly((p[0],p[3]))
C1 = 10E-9
C2 = 1E-9
R2 = 10e3
R1 = (-R2*C2)/(C1-a[1]*C1*R2*C2)

# R = sympy.symbols('R')
# equation = sympy.Eq((R*R2*C1*C2) ** (0.5)/(R*C1+R2*C2+R*C1*(1-K)),Q)
# R = sympy.solve(equation)

print(f'R1 = {R1}')
print(f'R2 = {R2}')
print(f'C1 = {C1}')
print(f'C2 = {C2}')
