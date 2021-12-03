from utils import *
import numpy as np


print("************************ TEST DE LA NORMALISATION ************************")

#génération d'un vecteur nommé x de 10( = size) éléments aléatoires qui sont entre -56( = low) et 20( = high). Ces élements sont arbitraires
x = np.random.randint( low = -56,high = 20, size=200)

#affichage de ce vecteur
print("x = ",x)
print('')

#Utilisation de la fonction de normalisation
xnorm = normalisation(x)

#Affichage du signal normalisé
print("normalized_x",xnorm)
print('')

'''
print("************************ TEST DE LA DIVISION ************************")

y = split(signal = test,Fe = 10,Tw = 5, Tss = 20)

print(y)
'''

print("************************ ENERGIE DU SIGNAL ************************")

E = signalenergy(x)
print(E)

