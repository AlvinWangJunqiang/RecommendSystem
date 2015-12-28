# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:41:06 2015

@author: Ldy
"""

import numpy as np
from factions import *


news_hoter= np.load('../data/news_hoter.npy').item()
news_hoter=dict_sort(news_hoter)

#tran_user_fre=np.load('../data/tran_user_fre.npy')
#tran_user_fre=list(tran_user_fre)
##print type(tran_user_fre)
#hot_user=set( get_key(count_list(tran_user_fre),100))#,type(tran_user_fre)
#np.save('../data/hot_user.npy', hot_user)

#hotest_100=dict(news_hoter[0:100])
#np.save('../data/hotest_100_news.npy',hotest_100)
same_user=np.load('../data/same_user.npy').item()
#print same_user
test_user_id=np.load('../data/test_user_id.npy').item()
use_list=[]
for use in test_user_id:
    if use not in same_user:
        use_list.append(use)

user_news=np.load('../data/user_news.npy').item()

print list(use_list)
#tran_user_id=np.load('../data/tran_user_id.npy').item()
#
#diff_user=set()
#for use in tran_user_id:
#    if use not in same_user:
#        diff_user.add(use)
#print len(tran_user_id),len(same_user),len(diff_user)
#np.save('../data/diff_user.npy', diff_user)
def calUUsim(k):
    U2U_tags={}
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
                    #print sameuse,usei,len(U2U_tags[sameuse]),U2U_tags[sameuse]==user_tags[sameuse]
                    
                else:
                    U2U_tags[sameuse]=user_tags[sameuse]
    return U2U_tags

#U2U_tags=calUUsim(4)

#np.save('../data/U2U_tags.npy', U2U_tags)