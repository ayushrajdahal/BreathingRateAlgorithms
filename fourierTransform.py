import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy

# plt.rcParams['figure.figsize']=[16,12]

plt.rcParams.update({'font.size':18})

df = pd.read_csv('sample1-gyro.csv')
# df = df[df['time']<4]		# Limits the observation time to 4s

f = np.array(df['wx'])
t = np.array(df['time'])

dt = 0.00227491293			# time interval betn two samples - Sampling frequency is 439.

# For computing the FFT
n = len(t)

fhat = np.fft.fft(f,n)				# Computes the fft
PSD = fhat * np.conj(fhat) / n 		# Power spectrum
freq = (1/(dt*n)) * np.arange(n)	# Create x-axis of frequencies
L = np.arange(1, np.floor(n/2), dtype='int')

plt.plot(freq[L], PSD[L], color='c', label='Noisy')           # plots the power spectrum

plt.legend()
# plt.show()        # to show the power spectrum plot

# Finding the peak:
peaks = scipy.signal.find_peaks(PSD[L], height=2)
peakFreq = freq[L][peaks[0][0]]
print(f'Peak frequency: {peakFreq}')
print(f'Breaths per minute: {peakFreq*60}')
