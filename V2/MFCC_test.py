import numpy as np
import scipy.signal as sgl
from utils import *
import matplotlib.pyplot as plt


def MFCC(signal,Fe):

   for i in range(len(signal)):

      #We pre-emphasize the signal with the same equation as 2.3 (but here alpha = 0.97) :
      sig_fil= signal.lfilter([1., -0.97],1, signal[i - 1])))
      signal_emp = np.array(sig_fil, 1, signal[i - 1]))



   #we split the signal :
   frameslist = split(signal_emp,Fe,15,30)

   #we apply a hamming window on every frame
   for i in range(len(frameslist)):
      frame_hamm = signal.hamming(len(frameslist[i]))
      frameslist[i] *= frame_hamm

   #the power spectrum of the signal :
   NDFT = 512
   P = []
   P= [(np.abs(signal.fft(frameslist[i]))**2)/NDFT for i in range(len(frameslist))]

   #we use Mel-Filter Bank
   fb = filterbanks.filter_banks(P,Fe)

   #we apply a Discrete Cosine Transform
   signal.dct(fb,norm = 'ortho')

   #in general, we take the first 13 values :
   listend = [fb[:,1:13]]

   return listend



F1 = 100
F2 = 500
F3 = 1000
S1 = []
S2 = []
S3 = []
Somme = []
Fe = 16000 

for t in range(1000):
    S1.append(np.sin(2*np.pi*F1*(t/Fe)))
    S2.append(np.sin(2*np.pi*F2*(t/Fe)))
    S3.append(np.sin(2*np.pi*F3*(t/Fe)))

l = MFCC(S1,Fe)
   
print("f1 = ",l)
#print("f2 = "+str(MFCC(s2,fe)))
#print("f3 = "+str(MFCC(s3,fe)))