from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

Fn = 22e3
fc = 2*np.pi*Fn
ordem = 8
Av = 1

z, p, k = signal.butter(ordem, fc, 'low', analog=True, output='zpk')
R3 = 10E3
RB = 100e3
C = 1E-9
transfer_func = [1] 
for N in range(int(ordem/2)):
    a = np.poly((p[0+N], p[-1-N]))
    transfer_func = np.convolve(transfer_func, a)
    Wc_square = a[2]
    Wc = np.sqrt(a[2])
    Q = Wc/a[1]
    K = 3.0 - 1/Q
    R = 1/(Wc*C)
    R4 = R3*(K-1)
    Av = K*Av
    print(f'Estagio {N+1}')
    print(f'R = {R}')
    print(f'R3 = {R3}')
    print(f'R4 = {R4}')
    print(f'C2 = {C}')
    print(f'Wc = {Wc}')
    print(f'Q = {Q}')
    print(f'K = {K}')
    print(f'Funcao de trasferencia = {a}\n\n')

RF = RB*(Av-1)
print(f'RF = {RF}') 
print(f'Ganho total = {Av}')
print(f'Equação geral = {k,transfer_func}')

w, h = signal.freqs([k], transfer_func)
plt.semilogx(w/(2*np.pi), 20 * np.log10(abs(h)), label=f'Ordem = {ordem}')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(Fn, color='green')  # cutoff frequency
plt.legend(loc='upper right')
plt.show()
