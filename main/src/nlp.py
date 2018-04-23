# -*- coding:utf-8 -*-
"""
@Time:2018/4/20 20:06
@Author:yuhongchao
"""
#这个是文本多样性

def lexical_diversity(text):
    return len(text) / len(set(text))

def precentage(count , total):
    return 100*count/total

