import numpy as np
import matplotlib.pyplot as plt

def acorr_signal(amp, frek, beta):
    return amp**2 / 2 * np.cos(frek*beta)

def acorr_noise(amp, frek, beta):
    return amp * np.sin(frek*beta) / beta

Amp_signal = 1.4*10**(-3)
frek_signal = 5000 #Hz

PSD_noise = 100 * 10 ** (-12)
frek_noise = 10**(6) #Hz

mul = 10
beta = (np.pi/frek_noise)*np.array([i for i in range(1,1000)])

acorr_combined = acorr_signal(Amp_signal, frek_signal, beta) + acorr_noise(PSD_noise, frek_noise, beta)

plt.plot(beta, acorr_combined)
plt.grid(True)
plt.show()
