# encoding=utf-8
import pandas as pd
import numpy as np
import time
import os
import jieba.analyse


def readfile(filename, sep, headers=None, names=None, septime="2014-03-20 23:59:00"):
    '''

    :param filename: The file which stores the data to be used
    :param sep: The delimitador to separate items
    :param headers: headers
    :param names: data col title names
    :param septime: the time to sep data
    :return: The data before sep time and after sep time
    '''

    raw_data = pd.read_table(filename, sep='\t', header=None, names=names).dropna(how='any')

    read_times = raw_data['read_time']
    sep_time = "2014-03-20 23:59:00"
    time_array = time.strptime(sep_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))

    index_before_sep_time = read_times.index[read_times < timestamp]
    index_after_sep_time = read_times.index[read_times >= timestamp]

    training_data = raw_data.drop(index_after_sep_time)
    testing_data = raw_data.drop(index_before_sep_time)

    return raw_data, training_data, testing_data


def getFreqDict(data, id, content):
    '''

    :param data:  The DataFrame where id and content exist
    :param id: The id of news
    :param content: The content of news
    :return: The frequence dict of each news
    '''

    news_id_content = data.loc[:, [id, content]].drop_duplicates().values

    freq_dict = {}
    for id, content in news_id_content:
        freq_dict[id] = set(jieba.analyse.extract_tags(content, topK=10))
    return freq_dict


def get_user_feature(file_name, training_data):
    same_user = np.load(file_name).item()
    user_id_news = training_data.loc[:, ['user_id', 'news_content']]
    grouped = user_id_news.groupby('user_id')
    for name, value in grouped:
        print name


if __name__ == '__main__':
    filename = '../data/user_click_data.txt'
    sep = '\t'
    names = ['user_id', 'news_id', 'read_time', 'news_title', 'news_content', 'news_publi_time']
    raw_data, training_data, testing_data = readfile(filename, sep, names=names)

    filepath = '../data/training_data_freq_dict.npy'
    if not os.path.exists(filepath):
        training_data_freq_dict = getFreqDict(training_data, 'news_id', 'news_content')
        np.save(filepath, training_data_freq_dict)
    freqdict = np.load(filepath)

    get_user_feature('../data/same_user.npy', training_data)
