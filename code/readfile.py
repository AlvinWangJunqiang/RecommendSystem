import collections
import pandas as pd
import time
import numpy as np

def readfile(filename, sep, headers=None, names=None, septime = "2014-03-20 23:59:00"):
    '''

    :param filename: The file which stores the data to be used
    :param sep: The delimitador to separate items
    :param headers: headers
    :param names: data col title names
    :param septime: the time to sep data
    :return: The data before sep time and after sep time
    '''

    raw_data = pd.read_table(filename, sep='\t', header=None, names=names)
    read_times = raw_data['read_time']
    sep_time = "2014-03-20 23:59:00"
    time_array = time.strptime(sep_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))

    index_before_sep_time = read_times.index[read_times < timestamp]
    index_after_sep_time = read_times.index[read_times >= timestamp]

    training_data = raw_data.drop(index_after_sep_time)
    testing_data = raw_data.drop(index_before_sep_time)

    return training_data, testing_data

if __name__ == '__main__':
    filename = '../data/user_click_data.txt'
    sep = '\t'
    names = ['user_id', 'news_id', 'read_time', 'news_title', 'news_content', 'news_publi_time']
    training_data, testing_data = readfile(filename,sep,names=names)
    tran_news_id= list(training_data['news_id'].values)
    test_news_id= list(testing_data['news_id'].values)
    news_id_list=tran_news_id+test_news_id
    #print len(news_id_list)
    test_user=set(list(testing_data['user_id'].values))
    tran_user=set(list(training_data['user_id'].values))
    same_user=set()
    for user in test_user:
        if user in tran_user:
            same_user.add(user)
    print same_user,len(same_user),len(test_user)
    np.save('../data/same_user.npy', same_user)
    counter=collections.Counter(news_id_list)
    news_hoter=dict(counter)
    #print news_hoter[100648598]
    np.save('news_hoter.npy', news_hoter)

