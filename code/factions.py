# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:06:08 2015

@author: Ldy
"""
from operator import itemgetter
import numpy as np
def calsim(VecA,VecB):
    Vsum=0.
    MAsum=0.
    MBsum=0.
    for i in xrange  (len(VecA)):
        Vsum=Vsum+VecA[i]*VecB[i]
        MAsum=MAsum+VecA[i]**2
        MBsum=MBsum+VecB[i]**2
    if MAsum==0 or MBsum==0:
        sim=0
    else:
        sim=Vsum/((MAsum**0.5)*(MBsum**0.5))
    return sim
A=[1,0,1]
B=[-2,0,-2]
print calsim(A,B)    

def tagssim(SetA,SetB):
    sim=0
    for key in SetA:
        if key in SetB:
            sim=sim+1
    return sim

a=set(A)
b=set(B)
print tagssim(a,b)

news_hoter= np.load('../data/news_hoter.npy').item()
news_hoter=sorted(news_hoter.items(), key=itemgetter(1), reverse=True)
hotest_100=dict(news_hoter[0:100])














    
    