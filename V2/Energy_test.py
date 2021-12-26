# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 03:47:00 2021

@author: gilbe
"""

from Utilss import Energy


#test que des valeurs positive ou nulle 
SignalA = [0, 1, 2, 3, 4, 5]
if (Energy(SignalA)==55):
    print("Good")
else: print("Error")

#test avec des valeurs négatives et les floats
SignalB = [0, -1, -2, -3, 4.2, -5]
if (Energy(SignalB)==56.64):
    print("Good")
else: print("Error")

#test avec que des valeurs nulles 
SignalC = [0, 0, 0, 0, 0]
if (Energy(SignalC)==0):
    print("Good")
else: print("Error")


Signal = [0, -1, -2, -3, -4, -5, 6, 7, 8]
energysignal= Energy(Signal)

def testenergy(energysignal):
    
    for value in range(energysignal):
        if(value<0):
            return "Error"
            break
    return "Tout est bon"

print(testenergy(energysignal))