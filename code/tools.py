# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:41:06 2015

@author: Ldy
"""

from factions import *

news_hoter = np.load('../data/news_hoter.npy').item()
news_hoter = dict_sort(news_hoter)

same_user = np.load('../data/same_user.npy').item()

test_user_id = np.load('../data/test_user_id.npy').item()
use_list = []
for use in test_user_id:
    if use not in same_user:
        use_list.append(use)

user_news = np.load('../data/user_news.npy').item()

print list(use_list)


def calUUsim(k):
    U2U_tags = {}
    usei = 0
    for sameuse in same_user:
        usei = usei + 1
        sameusej = 0
        for diffuse in hot_user:

            if sameuse in user_tags.keys() and diffuse in user_tags.keys():
                sim = tagssim(user_tags[sameuse], user_tags[diffuse])
                if sim >= k:

                    sameusej = sameusej + 1

                    U2U_tags[sameuse] = set(list(user_tags[sameuse]) + list(user_tags[diffuse]))


                else:
                    U2U_tags[sameuse] = user_tags[sameuse]
    return U2U_tags
