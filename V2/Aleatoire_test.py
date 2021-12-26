# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 05:04:16 2021

@author: gilbe
"""
import random

def FichierAléatoire():
    #On choisit entre 001-593 
    centaine = random.randint(0, 5)
    dizaine = random.randint(0, 9)
    
    #Ici on développe le cas précis de 001-009
    if ((centaine == 0) and (dizaine==0)):
            unite=random.randint(1,9)
            
    #Pareil pour le cas 590-593
    elif(centaine == 5 and dizaine == 9):
       unite=random.randint(0, 3)
    else:
        unite = random.randint(0, 9)
    #Cela permet de générer le nom du fichier
    NombreTest = centaine *100 + dizaine *10 + unite
    return NombreTest

    i = 1
    
    while i < 400: 
        NombreTest = FichierAléatoire()
        if ((NombreTest>593) or (NombreTest<0)):
            print("Error")
        i+=1