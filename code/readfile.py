# encoding=utf-8
import pandas as pd
import numpy as np
import time
import os
import jieba.analyse
import jieba.posseg as pseg


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


def createFreqDict(file_name, data):
    '''

    :param data:  The DataFrame where id and content exist
    :param id: The id of news
    :param content: The content of news
    :return: The frequence dict of each news
    '''

    id = 'news_id'
    content = 'news_content'
    news_id_content = data.loc[:, [id, content]].drop_duplicates().values

    freq_dict = {}
    for id, content in news_id_content:
        freq_dict[id] = set(jieba.analyse.extract_tags(content, topK=10))

    np.save(file_name, freq_dict)


def create_user_feature(file_name, training_data):
    # same_user = np.load(file_name).item()
    user_id_news = training_data.loc[:, ['user_id', 'news_content']]
    grouped = user_id_news.groupby('user_id')
    user_dict = {}
    counter = 0
    for name, df in grouped:
        strs = [content for id, content in df.values]
        strs = '.'.join(strs)
        features = set(jieba.analyse.extract_tags(strs, topK=10))
        counter += 1
        print counter
        user_dict[name] = features
    np.save(file_name, user_dict)


if __name__ == '__main__':
    filename = '../data/user_click_data.txt'
    sep = '\t'
    names = ['user_id', 'news_id', 'read_time', 'news_title', 'news_content', 'news_publi_time']
    raw_data, training_data, testing_data = readfile(filename, sep, names=names)

    filepath = '../data/testing_data_freq_dict.npy'
    if not os.path.exists(filepath):
        createFreqDict(file_name=filepath, data=testing_data)

    feature_path = '../data/user_feature.npy'
    if not os.path.exists(feature_path):
        create_user_feature(feature_path, training_data)
    user_feature = np.load(feature_path).item()

    # strstr = "北京天南门发生了暴恐事件, 很多人被打死了,天空飘舞着雪白的内裤和胸罩"
    # words = pseg.cut(strstr)
