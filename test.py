from utils import *
import matplotlib.pyplot as plt


print("********************** TEST DE LA NORMALISATION **********************")

#génération d'un vecteur nommé x de 10( = size) éléments aléatoires qui sont entre -30( = low) et 30( = high). Ces élements sont arbitraires
x = np.random.randint( low = -30,high = 30, size=10)
print("x = ",'\n',x,'\n')

#Utilisation de la fonction de normalisation
xnorm = normalisation(x)
print("normalized_x : ",'\n',xnorm,'\n')

ok = True
it_problem = []

for i in range(len(xnorm)):
    if(xnorm[i] <= 1 and xnorm[i] >= -1):
        continue

    else :
        ok = False
        it_problem.append(i)

if ok == True :print("On est entre -1 et 1")
if ok == False:print("ERROR : On n'est pas entre -1 et 1 en" , it_problem)

max = np.max(np.abs(x))
it_max = np.where(np.abs(x) == max)

if np.abs(xnorm[it_max]) == 1:
    print("A la position max(rsp. min), la valeur est 1")
    ok = True


else:
    print("ERROR : A la position max(rsp. min), la valeur n'est pas 1")
    ok  = False

print('\n')
if (ok == True):print("LA NORMALISATION FONCTIONNE CORRECTEMENT")
else : print("IL Y A DES ERREURS ")
print('\n')
print('\n')

from scipy.io import wavfile
samplerate, data = wavfile.read('./arctic_a0007.wav')


print("s : ", samplerate)
print("data",data)

plt.plot(data)
plt.show()

datanorm = normalisation(data)

plt.plot(datanorm)
plt.show()




print("********************** ENERGIE DU SIGNAL **********************")

E = signalenergy(x)
print(E)


#test formant et split Louis


print("******************** MFCC ***************************")

F1 = 100
F2 = 500
F3 = 1000
S1 = []
S2 = []
S3 = []
Somme = []
Fe = 16000

for t in range(1000):
    S1.append(np.sin(2 * np.pi * F1 * (t / Fe)))
    S2.append(np.sin(2 * np.pi * F2 * (t / Fe)))
    S3.append(np.sin(2 * np.pi * F3 * (t / Fe)))

l = MFCC(S1, Fe)

print("f1 = ", l)
# print("f2 = "+str(MFCC(s2,fe)))
# print("f3 = "+str(MFCC(s3,fe)))