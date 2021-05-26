import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

N = 10 ** 4
snr_range = np.arange(0, 15, 1)
BER_simulated = np.zeros(len(snr_range))
bit = np.random.randint(0, 2, N)

print(bit)
# BPSK
transmitted_signal = 2 * bit - 1
print(transmitted_signal)
for i, snr in enumerate(snr_range):
    linear_snr = 10 ** (snr / 10)
    signal_power = sum(abs(transmitted_signal)) / len(transmitted_signal)
    noise_power = signal_power / linear_snr
    noise = np.sqrt(noise_power) * np.random.standard_normal(N)

    print(noise, 'noise')
    recieved_signal = transmitted_signal + noise
    estimated_signal = (recieved_signal >= 0).astype(int)
    print(recieved_signal, 'rec')
    print(estimated_signal, 'est')
    BER_simulated[i] = np.sum(estimated_signal != bit) / N

print(BER_simulated)
BER_THEORITICAL = 0.5 * erfc(np.sqrt(10 ** (snr_range / 10)))

# Plotting

plt.semilogy(snr_range, BER_THEORITICAL, marker='', linestyle='-', label="THEORITICAL BER")
plt.semilogy(snr_range, BER_simulated, color='r', marker='o', linestyle='', label="PRACTICAL BER")
plt.legend()
plt.show()
