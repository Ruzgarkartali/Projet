# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 03:33:33 2021

@author: gilbe
"""

import numpy as np

def normalisation(signal):

   # on met tous les éléments du tableau en valeur absolue pour avoir plus facilement accès à la valeur la plus grande
   abs_signal = np.abs(signal)

   #on trouve la valeur la plus grande
   max = np.max(abs_signal)

   #on divise chaque valeur par le max (pour ainsi avoir un pourcentage)
   normalized_signal = signal/max

   return normalized_signal



#1er test simple
signalA = [5, 10, 15,20]
if (normalisation(signalA)==[0.25, 0.5, 0.75, 1]):
    print("good")
else:
    print("problem")
    
#2eme test avec des négatifs
signalB = [4, 8, -12, 16]
if (normalisation(signalB)==[0.25, 0.5, -0.75, 1]):
    print("good")
else:
    print("problem")
    

signal = [1, 2, 3, 4, 1, 2, 3, -4]
normsignal = normalisation(signal)

def testnormalisation (normsignal):
 A = len(normsignal)
 
 for i in range(A):
     
  if ((normsignal[i]<-1)or(normsignal[i]>1)):
      return "Erreur dans la valeur"
  
 if ((1 not in normsignal) and (-1 not in normsignal)):
        return" Erreur dans les maximum"
        
 else:
         return "Tout fonctionne bien"
print(testnormalisation(normsignal))