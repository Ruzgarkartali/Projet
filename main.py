import utils
import numpy as np


print("************************ TEST DE LA NORMALISATION ************************")

#génération d'un vecteur nommé x de 10( = size) éléments aléatoires qui sont entre -56( = low) et 20( = high). Ces élements sont arbitraires
x = np.random.randint( low = -56,high = 20, size=10)

#affichage de ce vecteur
print("x = ",x)
print('')

#Utilisation de la fonction de normalisation
normalized_x = utils.normalisation(x)

#Affichage du signal normalisé
print("normalized_x",normalized_x)
print('')

print("************************ TEST DE LA DIVISION ************************")

