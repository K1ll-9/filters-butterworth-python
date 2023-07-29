#!/usr/local/bin/python3

import wave
import struct

from scipy.fft import fft, fftfreq
from scipy.signal import butter, lfilter, freqz, sosfilt
import scipy.fftpack
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt


INFILE="data/loopbuffer.raw"
OUTFILE="data/filteredbuffer.raw"

FR=44100

signal = []
filtered = []

mpl.style.use('dark_background');

#
# Print non filtered loop signal
#
fig1, axs1 = plt.subplots(2, 2, figsize=(15, 10))

with open(INFILE, "r") as outputs:
  for line in outputs.readlines():
    signal += [float(line)]

t = np.arange(0, len(signal)) / FR
axs1[0, 0].plot(t, signal, label='Raw loop signal', color='C3')
axs1[0, 0].set_title("Raw signal waveform 82 Hz")
axs1[0, 0].grid(color='grey', linewidth=1, linestyle='--',)

# Print dfft spectrum
yf = np.fft.fft(signal)
xf = np.fft.fftfreq(len(yf), 1/FR)[:len(signal)//2]

axs1[1, 0].plot(xf, np.abs(yf[0:len(signal)//2]), color='C5')
axs1[1, 0].axis([0, 2000, 0, 17000])
axs1[1, 0].set_title("Raw loop signal spectrum")


#
# filtered signal plot
#

with open(OUTFILE, "r") as outputs:
  for line in outputs.readlines():
    filtered += [float(line)]

t = np.arange(0, len(filtered)) / 48000

FC=205
ORDER=4
axs1[0, 1].plot(t, filtered, label='Filtered signal', color='C3')
axs1[0, 1].set_title("Filtered signal waveform fc:"+ str(FC) +" Hz")
axs1[0, 1].grid(color='grey', linewidth=1, linestyle='--',)

# Print dfft spectrum of butter_filtered signal
yf = np.fft.fft(filtered)
xf = np.fft.fftfreq(len(yf), 1/FR)[:len(filtered)//2]

axs1[1, 1].plot(xf, np.abs(yf[0:len(filtered)//2]), color='C5')
axs1[1, 1].axis([0, 2000, 0, 17000])
axs1[1, 1].set_title("Filtered signal spectrum (lowpass butter "+ str(ORDER) +"th order - fc:"+str(FC)+"Hz")

plt.show()