# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 00:42:22 2021

@author: gilbe
"""

import numpy as np
import scipy.signal as sgl
from utils import lpc_ref
import matplotlib.pyplot as plt

Signal=[]

def formant(Signal, Fe):
   f = []
   #temp = []

   HPfilter = np.array(sgl.lfilter([1., -0.67], 1, Signal))


   # 3
   frame_hamm = HPfilter * sgl.hamming(len(HPfilter))

   # 4
   lpc_coeff = lpc_ref(frame_hamm, (2 + int(Fe / 1000)))

   # 5
   complex = np.roots(lpc_coeff)

   complex = [r for r in complex if np.imag(r) > 0]

   angles = np.array(np.angle(complex))

   f = np.array(np.unique(abs(angles * (Fe / (2 * np.pi)))))

   #plt.plot(f)
   f.tolist()
   f.sort()

   #angles_sort = sorted(angles * (Fe / (2 * np.pi)))
   
    
   '''
   f.append(sorted(angles *(Fe/(2*np.pi))))  
   
      for j in range(len(f[i])):
          if f[i][j] != 0 : 
              f[i] = f[i][j]
              break
    
    Moyformant= 0
    M = 0
    for j in range(len(f)):
        Moyformant += f[j]
        M  +=1
    if M != 0:
        Moyformant = Moyformant/M
        
       '''

   return f


F1 = 100
F2 = 200
F3 = 1000
S1 = []
S2 = []
S3 = []
Fe = 16000 
somme = []

for t in range(1000):   
    S1.append(np.sin(2*np.pi*F1*(t/Fe)))
    S2.append(np.sin(2*np.pi*F2*(t/Fe)))
    S3.append(np.sin(2*np.pi*F3*(t/Fe)))
   
print("f1 = "+str(formant(S1,Fe)))
print("f2 = "+str(formant(S2,Fe)))
print("f3 = "+str(formant(S3,Fe)))
