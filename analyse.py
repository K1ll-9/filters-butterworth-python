#!/usr/local/bin/python3

import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import itertools

#print('Number of arguments:', len(sys.argv), 'arguments.')

if len(sys.argv)<2 :
  print("Missing file name as arg.")
  exit(1)

print('Opening filename:', str(sys.argv[1]))

INFILE=str(sys.argv[1])

FR=44100

signal = []

mpl.style.use('dark_background');
fig1, axs1 = plt.subplots(2, 2, figsize=(15, 10))

with open(INFILE, "r") as outputs:
  for line in outputs.readlines():
    signal += [float(line)]


#######################################################################@
# Used loop

t = np.arange(0, len(signal)) / FR
axs1[0, 0].plot(t, signal, label='Raw loop signal', color='C3')
axs1[0, 0].set_title("Raw signal waveform")
axs1[0, 0].grid(color='grey', linewidth=1, linestyle='--',)

# Print dfft spectrum
yf = np.fft.fft(signal)
xf = np.fft.fftfreq(len(yf), 1/FR)[:len(signal)//2]

axs1[1, 0].plot(xf, np.abs(yf[0:len(signal)//2]), color='C5')
axs1[1, 0].axis([0, 2000, 0, 17000])
axs1[1, 0].set_title("Raw loop signal spectrum")

#######################################################################@
# repeated loop
#def repeat(lst, count):
#  return np.stack([lst for _ in range(count)], axis=0)

def repeat(lst, count):
  rlist = []
  for _ in range(count):
    for i in range(len(lst)):
      rlist.append(lst[i])
  return rlist
      

#rep_signal = repeat(signal, 2)
rep_signal = repeat(signal, 10)

#print("Raw_signal: "+str(signal))
#print("Rep_signal: "+str(rep_signal))

t = np.arange(0, len(rep_signal)) / FR
axs1[0, 1].plot(t, rep_signal, label='Repeated loop signal', color='C3')
axs1[0, 1].set_title("Repeated signal waveform")
axs1[0, 1].grid(color='grey', linewidth=1, linestyle='--',)

# Print dfft spectrum
yf = np.fft.fft(rep_signal)
xf = np.fft.fftfreq(len(yf), 1/FR)[:len(rep_signal)//2]

axs1[1, 1].plot(xf, np.abs(yf[0:len(rep_signal)//2]), color='C5')
axs1[1, 1].axis([0, 2000, 0, 200])
axs1[1, 1].set_title("Looped signal spectrum")


plt.show()