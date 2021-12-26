import numpy as np
import scipy.signal as sgl
from utils import split,filter_banks,dct
import matplotlib.pyplot as plt


def MFCC(Signal, Fe):
    Signal = np.asarray(Signal)
    
        
    Signal_emp = np.array(Signal.lfilter([1., -0.97], 1, Signal))
    Signal_emp.tolist()
    
    # 2
    frameslist = split(Signal_emp, Fe, 15, 30)
    frameslist = np.array(frameslist)
    
    # 3
    for i in range(len(frameslist)):
      frame_hamm = sgl.hamming(len(frameslist[i]))
      frameslist[i] *= frame_hamm

    # 4
    NFFT = 512
    P = []
    P= [(np.abs(Signal.fft(frameslist[i]))**2)/NFFT for i in range(len(frameslist))]


    # 5
    Temp=(len(frameslist[0])*2)-1
    Filterbanks = filter_banks(P, Fe, nfilt = 40, NFFT = Temp) 
    
    # 6
    MFCCVect = dct(Filterbanks,type=2,axis=1,norm ='ortho') 
    # 7
    LastMFCC = MFCCVect[:, 0:12]
    plt.plot(MFCCVect)
    return LastMFCC    

F1 = 100
F2 = 500
F3 = 1000
S1 = []
S2 = []
S3 = []
Somme = []
Fe = 16000 

for t in range(1000):
    S1.append(np.sin(2*np.pi*F1*(t/Fe)))
    S2.append(np.sin(2*np.pi*F2*(t/Fe)))
    S3.append(np.sin(2*np.pi*F3*(t/Fe)))
   
print("f1 = "+str(MFCC(S1,Fe)))
#print("f2 = "+str(MFCC(s2,fe)))
#print("f3 = "+str(MFCC(s3,fe)))