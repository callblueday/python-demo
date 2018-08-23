#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
from addict import Dict

def dictionary_combine_key(dictionary, newJson, mykey):
    for key, value in dictionary.items():
        try:
            mykey.append(key)
            dictionary_combine_key(value, newJson, mykey)
        except AttributeError:
            key = '.'.join(mykey)
            print(str(key) + ' : ' + str(value))
            newJson[key] = value
            mykey.pop()
    return newJson

def serialize(filepath):
    newJson = Dict()
    mykey = []
    f = open(filepath)
    content = json.load(f)
    result = dictionary_combine_key(content, newJson, mykey)
    return result

# a=serialize('test-data/en.json')
v1 = serialize('v1.json')
# v2 = serialize('v2.json')
# print(v1)


# 比对 v1 和 v2【以 v1 为基础，逐行比对 v2】: v1 是本地，v2 crowdin 翻译而来
#     * 改动的：使用 v2 文件
#     * 相同的：跳过
#     * 新增的：跳过
def compare(dict1, dict2):
    # print(dict1)
    # print(dict2)
    for key, value in dict1.items():
        print(dict2[key] == value)
        if dict2[key]:
            if dict2[key] != value:
                dict1[key] = dict2[key]
    return dict1


def write_to_file(filepath, dictionary):
    # 将最新文件写入 json
    jsObj = json.dumps(dictionary, indent=4, sort_keys=False, ensure_ascii=False)
    fileObject = open(filepath, 'w')
    fileObject.write(jsObj)
    fileObject.close()

# result = compare(v1, v2)
# write_to_file('./result.json', result)


# keys = ["a", "b", "c"]
# a = getKey(keys, 'nihao')
def getKey(keys, value):
    while len(keys) > 0:
        temp = {}
        li = keys.pop()
        temp[li] = value
        value = temp
    return temp


def deserialize(dictionary):
    mydict = Dict({})
    for key, value in dictionary.items():
        keys = key.split('.')
        temp = Dict(getKey(keys, value))
        mydict.update(temp)
    return mydict

# print(v1)
# compareResult = deserialize(v1)
# print(compareResult)

# write_to_file('./result.json', compareResult)