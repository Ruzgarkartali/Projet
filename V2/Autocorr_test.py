# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 05:21:08 2021

@author: gilbe
"""

import numpy as np

#from Utilss import Energy
from Utilss import xcorr
import scipy.signal as sgl
import matplotlib.pyplot as plt


def Autocorr(Es, Signal, Fe):

    #initialisation
    Pitchlist = [] 
    #Energie = Energy(Signal)
    
    
    SignalArr = np.array(Signal)                         #Passer en "array/list" facilite les calculs 
    lags, c = xcorr(SignalArr, maxlags = int(Fe/50))          #on utilise la fonction donner sur moodle 
    #plt.plot(c)
                                                                     #on cherche les maxima
    maxima, value = sgl.find_peaks(c, height=0, distance=45 ) #on utilise la fonction"find peaks" de la librairie "scipy", la distance permet d'éviter des erreurs
    Mvalue = value['peak_heights']                            #L'affichage contient {'peak_heights':array([... ])}, on veut que "array"
                                                                     # "maxima" = localisation des pics (selon x)
    maxima = maxima.tolist()                                  # "value" = hauteur des pics
                                                                     #on utilise la fonction "tolist()" pour convertir maxima en une "list"
    Mvalue, maxima = zip(*sorted(zip(Mvalue, maxima)))        #triage croissant
    D = len(maxima)
    Dist = np.abs(maxima[D-1] - maxima[D-2])                  #on calcule la distance (selon x) séparant les 2 plus grand maxima (en valeur absolue)             
    Ffdmtl = Fe/Dist                                          #on calcul la frequence fondamentale                                
    Pitchlist.append(Ffdmtl)                                  #on l'ajoute à la liste         
           
                    
    PitchArr = np.array(Pitchlist)                                    #Encore une fois, passer en "array/list" facilite les calculs
    PitchArrMoy = abs(np.mean(PitchArr))                              #Calcul la moyenne  

    return Pitchlist




F1 = 100
F2 = 200
F3 = 300
S1 = []
S2 = []
S3 = []
Fe = 16000 
somme = []

for t in range(800):
    S1.append(np.sin(2*np.pi*F1*(t/Fe)))
    S2.append(np.sin(2*np.pi*F2*(t/Fe)))
    S3.append(np.sin(2*np.pi*F3*(t/Fe)))
   
print("F1 = "+str(Autocorr(S1,Fe,100)))
print("F2 = "+str(Autocorr(S2,Fe,100)))
print("F3 = "+str(Autocorr(S3,Fe,100)))