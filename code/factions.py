# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:06:08 2015

@author: Ldy
"""
import collections
from operator import itemgetter
import numpy as np
from readfile import get_hot_news_rank,readfile
#import pandas as pd

oneday=24*3600


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


hotest_100=dict(news_hoter[0:100])
np.save('../data/hotest_100_news.npy',hotest_100)
same_user=np.load('../data/same_user.npy').item()
test_user_id=np.load('../data/test_user_id.npy').item()
use_list=[]
for use in test_user_id:
    if use not in same_user:
        use_list.append(use)
#print use_list


user_tags=np.load('../data/user_feature.npy').item()

news_tags=np.load('../data/testing_data_freq_dict.npy').item()


user_time=np.load('../data/user_time_test_table.npy').item()




    
def cbr(user_id):
    sims={}
    for key in news_tags.keys():
        sims[key]=tagssim(user_tags[user_id],news_tags[key])
    return sims    



    
def content_base(data, user_id,k=5):
    if user_id in user_tags.keys():
        sims=cbr(user_id)
        return get_key(sims,k)
    else:
        #print 1
        return get_hot_news_rank(data, k=k, time_end = user_time[user_id],days=1)

if __name__ == '__main__':
    filename = '../data/user_click_data.txt'
    sep = '\t'
    names = ['user_id', 'news_id', 'read_time', 'news_title', 'news_content', 'news_publi_time']
    raw_data, training_data, testing_data = readfile(filename, sep, names=names)    
    sims=content_base(raw_data,10657711,10)
    print sims






