# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:06:08 2015

@author: Ldy
"""

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