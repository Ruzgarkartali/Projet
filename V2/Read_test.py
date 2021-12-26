import random
from scipy.io.wavfile import read


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
    Nomfichier = "arctic_a0%i%i%i.wav" % (centaine, dizaine, unite)
    return Nomfichier

def ReadFiles(choix):
    if (choix == 'male' or choix == 'female'):
        if (choix == 'male'):
            choix = '../cmu_us_bdl_arctic/wav/%s'
        elif (choix == 'female'):
            choix = '../cmu_us_slt_arctic/wav/%s'
        
        utterance = read(choix % (FichierAléatoire()))
        Fe = utterance[0]
        sig = utterance[1]
        Signal = sig.tolist()        
    else : 
        print('Choisissez entre "male" ou "female"')
        
    return Signal, Fe

def TestRead(Signal, Fe):
    if (Signal==[1, 1]):
        return"Error : liste vide"
        
    elif(Fe==0):
        return"Error : Fe pas prise"
        
    else:
        return"Good"
 
    
Fe = 0
Signal = [1, 1]    

Signal, Fe = ReadFiles("male")

print(TestRead(Signal, Fe))