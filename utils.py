import numpy as np


def normalization(signal):
    array = np.array(signal)
    #Chercher la valeur maximale du signal en valeur absolue
    absolute = np.abs(array)
    maxima = np.max(absolute)
    #Diviser tout les échantillons par la valeur maximale
    normsignal = array/maxima
    normsignal = normsignal.tolist()
    return normsignal