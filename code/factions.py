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
#print calsim(A,B)    

def tagssim(SetA,SetB):
    sim=0
    for key in SetA:
        if key in SetB:
            sim=sim+1
    return sim

def dict_sort(dic):
    return sorted(dic.items(), key=itemgetter(1), reverse=True)

a=set(A)
b=set(B)#
#print tagssim(a,b)

news_hoter= np.load('../data/news_hoter.npy').item()
news_hoter=dict_sort(news_hoter)
hotest_100=dict(news_hoter[0:100])
np.save('../data/hotest_100_news.npy',hotest_100)
same_user=np.load('../data/same_user.npy').item()
#print same_user,type(same_user)

hot_news_tags={'色情','AV'}
news_tags={1:{'色情','娱乐','时尚'},2:{'暴力','AV','游戏'},3:{'教育','财经','社会'}}
#print len(news_tags)
user_tags={310766:{'色情','时尚'}}

def find_hot_news(news_tags,hot_news_tags,k):
    hot_news={}
    for key in news_tags.keys():
        if tagssim(news_tags[key],hot_news_tags)>=k:
            hot_news[key]=news_tags[key]
    return hot_news

hot_news=find_hot_news(news_tags,hot_news_tags,1)
    


def cbr(user_id):
    sims={}
    for key in news_tags.keys():
        sims[key]=tagssim(user_tags[user_id],news_tags[key])
    return sims    

#def hot_re(read_time):
    
def content_base(user_id,read_time=0):
    if user_id in same_user:
        return cbr(user_id)
    else:
        return hot_re(read_time)

sims=content_base(310766)
print sims







