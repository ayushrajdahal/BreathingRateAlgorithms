import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy


df = pd.read_csv('SampleCsv.csv')
# df = pd.read_excel('SampleExcel.xlsx')
threshold = 0.001		# threshold for the peak finding algorithm
# df = df[df['time']<10]


def plot():
	
	plt.plot(df['time'], df['wx'])
	# plt.show()

	global filtered
	filtered = bandPassFilter(np.array(df['wx'])) 		# This is the filtered signal

	plt.plot(df['time'], filtered, linewidth=3)
	plt.show()


def bandPassFilter(signal):		# Filters out the noise using band pass filtering algorithm
	fs = 40000.0
	lowcut = 20.0
	highcut = 50.0
	
	nyq = 0.5*fs
	low = lowcut/nyq
	high = highcut/nyq

	order = 2

	b, a = scipy.signal.butter(order, [low, high], 'bandpass', analog=False)
	y = scipy.signal.filtfilt(b, a, signal, axis=0)

	return(y)


plot()


peaks = scipy.signal.find_peaks(filtered, height=threshold)
# print(peaks)

noOfPeaks = len(peaks[1]['peak_heights'])

print(f'Number of peaks in this sample: {noOfPeaks}')

breathRate = (noOfPeaks)/df['time'].max()*60
print(f'Breathing rate:{breathRate}')
