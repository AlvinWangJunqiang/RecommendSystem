# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:06:08 2015

@author: Ldy
"""
import collections
from operator import itemgetter
import numpy as np
lastday=24*3600
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

def tagssim(SetA,SetB):
    sim=0
    for key in SetA:
        if key in SetB:
            sim=sim+1
    return sim

def dict_sort(dic):
    return sorted(dic.items(), key=itemgetter(1), reverse=True)

def get_key(dic,k):
    return map(itemgetter(0), sorted(dic.items(), key=itemgetter(1), reverse=True))[:k]

def count_list(a):
    counter=collections.Counter(a)
    return dict(counter)

news_hoter= np.load('../data/news_hoter.npy').item()
news_hoter=dict_sort(news_hoter)
#print type(news_hoter),news_hoter
hotest_100=dict(news_hoter[0:100])
np.save('../data/hotest_100_news.npy',hotest_100)
same_user=np.load('../data/same_user.npy').item()
#print same_user
#print same_user,type(same_user)
#print len(news_tags)
#user_tags={310766:{'色情','时尚'}}

user_tags=np.load('../data/user_feature.npy').item()

news_tags=np.load('../data/testing_data_freq_dict.npy').item()

news_id2times=np.load('../data/newstotimes.npy')
print news_id2times

test_user_id=np.load('../data/test_user_id.npy').item()

#print user_tags[7979008]

def find_hot_news(news_tags,hot_news_tags,k):
    hot_news={}
    for key in news_tags.keys():
        if tagssim(news_tags[key],hot_news_tags)>=k:
            hot_news[key]=news_tags[key]
    return hot_news

#hot_news=find_hot_news(news_tags,hot_news_tags,1)
    
def cbr(user_id):
    sims={}
    for key in news_tags.keys():
        sims[key]=tagssim(user_tags[user_id],news_tags[key])
    return sims    
test=[(1,2),(1,2)]
def hot_re(news_id2times,read_time,k):
    news_id_list=[]
    for i in xrange(news_id2times):
        if read_time-lastday<news_id2times[i][1]<read_time:
            news_id_list.append(news_id2times[i][0])
    dic=count_list(news_id_list)
        
    return get_key(dic,k)
    
def content_base(user_id,read_time=0,k=5):
    if user_id in user_tags.keys():
        sims=cbr(user_id)
        return get_key(sims,k)
    else:
        return hot_re(news_id2times,read_time,k)

if __name__ == '__main__':
    sims=content_base(344047,0,4)
    print sims






