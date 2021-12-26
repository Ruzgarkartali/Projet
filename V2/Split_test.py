# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 03:38:19 2021

@author: gilbe
"""

from Utilss import split 


#Test Tw = Tss 
SignalA = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
FeA = 1000
TssA = 2
TwA = 2

if (split(SignalA, FeA, TwA, TssA)==[[1, 1], [0, 0], [1, 1], [0, 0], [1, 1]]):
    print ("Good")
else :
    print ("Error")

#Test Tw < Tss
SignalB = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
FeB = 1000
TssB = 4
TwB = 2

if (split(SignalB, FeB, TwB, TssB)==[[1, 1], [1, 1], [1, 1]]):
    print ("Good")
else :
    print ("Error")
      
   
#Test Tw > Tss
SignalC = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
FeC = 1000
TssC = 2
TwC = 4

if (split(SignalC, FeC, TwC, TssC)==0):
    print ("Good")
else :
    print ("Error")


#Test où Fe change
SignalD = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
FeD = 2000
TssD = 4
TwD = 2

if (split(SignalD, FeD, TwD, TssD)==[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]):
    print ("Good")
else :
    print ("Error")
    
    
#Test Tw = Tss = 0
SignalE = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
FeE = 1000
TssE = 0
TwE = 0

if (split(SignalE, FeE, TwE, TssE)==0):
    print ("Good")
else :
    print ("Error")
    

#Test Tw = 0 (pour Tss=0 on a Tss < Tw)
SignalF = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
FeF = 1000
TssF = 2
TwF = 0

if (split(SignalF, FeF, TwF, TssF)==0):
    print ("Good")
else :
    print ("Error")
    
    
#Test Fe = 0
SignalG = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
FeG = 0
TssG = 4
TwG = 2

if (split(SignalG, FeG, TwG, TssG)==0):
    print ("Good")
else :
    print ("Error")