from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

Fn = 22e3
fc = 2*np.pi*Fn
ordem = 2
rp = 0.5
rs = 33
z, p, k = signal.ellip(ordem, rp, rs, fc, 'low', analog=True, output='zpk')
Av = 1/k  # para normalizar o ganho
Av2 = 1/k  # para normalizar o ganho

R3 = 10E3  # resistor de ganho
RF = 1e3  # resistor constante para normalização do ganho
C = 1E-9
transfer_func_polos = [1]
transfer_func_zeros = [1]

for N in range(int(ordem/2)):
    a = np.poly((p[N], np.conjugate(p[N])))
    b = np.poly((z[N], np.conjugate(z[N])))
    transfer_func_polos = np.convolve(transfer_func_polos, a)
    transfer_func_zeros = np.convolve(transfer_func_zeros, b)
    Wc_square = a[2]
    Wc = np.sqrt(a[2])
    Q = Wc/a[1]
    K = 3.0 - 1/Q  # ganho por estagio
    R = 1/(Wc*C)
    R4 = R3*(K-1)
    adj = a[2]/b[2]
    Av = K*Av*adj  # ganho total
    Av2 = K*Av2  # ganho total
    RB = RF*Av  # resistor para normalização do ganho
    RB2 = RF*Av2  # resistor para normalização do ganho
    print(f'Estagio {N+1}')
    print(f'R = {R}')
    print(f'R3 = {R3}')
    print(f'R4 = {R4}')
    print(f'C2 = {C}')
    print(f'Wc = {Wc}')
    print(f'Q = {Q}')
    print(f'K = {K}')
    print(f'RB = {RB}')
    print(f'RB2 = {RB2}')
    print(f'Funcao de trasferencia = {b}{a}\n\n')
    Av = 1.0
    Av2 = 1.0

print(f'Equação geral = {k}{transfer_func_zeros,transfer_func_polos}')

w, h = signal.freqs(k*transfer_func_zeros, transfer_func_polos)
plt.semilogx(w/(2*np.pi), 20 * np.log10(abs(h)), label=f'Ordem = {ordem}')
plt.title('Respsosta em frequencia do filtro Eliptico')
plt.xlabel('Frequencia [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(Fn, color='green')  # cutoff frequency
plt.legend(loc='upper right')
plt.show()
