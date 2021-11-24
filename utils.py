import numpy as np
import sklearn as sk
from sklearn import preprocessing


# ************************ PRE PROCESSING ************************

# l'objectif de la normalisation est de réduire le vecteur signal pour que chaque donnée soit représenté comme un pourcentage
# de la plus grande(petite) valeur (pour ca qu'on aura un vecteur entre -1 et 1)

def normalisation(signal):

   # on met tous les éléments du tableau en valeur absolue pour avoir plus facilement accès à la valeur la plus grande
   abs_signal = np.abs(signal)

   #on trouve la valeur la plus grande
   max = np.max(abs_signal)

   #on divise chaque valeur par le max (pour ainsi avoir un pourcentage)
   normalized_signal = signal/max


   return normalized_signal




