# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:06:08 2015

@author: Ldy
"""
import collections
from operator import itemgetter
import numpy as np
from readfile import get_hot_news_rank
import pandas as pd



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



 
diff_user=np.load('../data/diff_user.npy').item()
#print len(diff_user)
user_tags=np.load('../data/user_feature.npy').item()
#print len(user_tags)
news_tags=np.load('../data/testing_data_freq_dict.npy').item()

user_time=np.load('../data/user_time_test_table.npy').item()

hot_user=np.load('../data/hot_user.npy').item()

U2U_tags=np.load('../data/U2U_tags.npy').item()

same_user=np.load('../data/same_user.npy').item()

user_news_dict=np.load('../data/user_news_dict.npy').item()
print type(user_news_dict)

def calUUsim(k):
    U2U_tags=user_tags
    usei=0
    for sameuse in same_user:
        usei=usei+1
        sameusej=0
        for diffuse in hot_user:
            
            if sameuse in user_tags.keys() and diffuse in user_tags.keys():
                sim=tagssim(user_tags[sameuse],user_tags[diffuse])
                if sim>=k:
                    
                    sameusej=sameusej+1
                    #print sameuse,usei,sameusej,sim
                    U2U_tags[sameuse]=set(list(user_tags[sameuse])+list(user_tags[diffuse]))
                    print sameuse,usei,len(U2U_tags[sameuse])#,U2U_tags[sameuse]==user_tags[sameuse]
    return U2U_tags


def cbr(user_id,tags_data):
    sims={}
    for key in news_tags.keys():
        sims[key]=tagssim(tags_data[user_id],news_tags[key])
    return sims    

def content_base(data, user_id,k=5):
    if user_id in user_tags.keys():
        sims=cbr(user_id,user_tags)
        #print 1
        return get_key(sims,k)
    else:
        #print 1
        return get_hot_news_rank(data, k=k, time_end = user_time[user_id],days=1)

def UUCF(data, user_id,k=5):
    if user_id in U2U_tags.keys():
        sims=cbr(user_id,U2U_tags)
        return get_key(sims,k)
    else:
        return get_hot_news_rank(data, k=k, time_end = user_time[user_id],days=1)

def Rs_test(k):
    n1=0
    user_num=0
    for user_id in user_news_dict.keys():
        i=0
        user_num=user_num+1
        print user_num
        result=set(content_base(raw_data,user_id,k))
        for news_id in result:
            if news_id in user_news_dict[user_id]:
                i=i+1
        m=0
        if len(user_news_dict[user_id])>k:
            m=k
        else:
            m=len(user_news_dict[user_id])
        if i>=m/2:
            n1=n1+1
    n2=0
    user_num=0
    for user_id in user_news_dict.keys():
        i=0
        user_num=user_num+1
        print user_num
        result=set(UUCF(raw_data,user_id,k))
        for news_id in result:
            if news_id in user_news_dict[user_id]:
                i=i+1
        m=0
        if len(user_news_dict[user_id])>k:
            m=k
        else:
            m=len(user_news_dict[user_id])
        if i>=m/2:
            n2=n2+1
    return n1,n2

if __name__ == '__main__':
    raw_data = pd.read_csv('../data/news_id_time_table.csv').loc[:,['news_id', 'read_time']] 
    print Rs_test(20)




