#!/usr/bin/env Python
# coding=utf-8

import os
import json
from addict import Dict

mydict = Dict({})

# 遍历目录
def gci(filepath):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            mergeFileWithLang(fi_d, fi)

# 读取文件，根据名称判断写入到哪个目标文件中
def mergeFileWithLang(filepath, filename):
    print(filename)
    f = open(filepath)
    content = Dict(json.load(f))
    mydict.update(content)

def write_to_file(filepath, dictionary):
    # 将最新文件写入 json
    jsObj = json.dumps(dictionary, indent=4, sort_keys=False, ensure_ascii=False)
    fileObject = open(filepath, 'w')
    fileObject.write(jsObj)
    fileObject.close()

# 遍历目录下的文件名
def get_file_names(file_dir):
    target_file_name = []
    for root, dirs, files in os.walk(file_dir):
        target_file_name += files
    return list(set(target_file_name))

to_merge_dir = './WAIT_MERGE'       # 待合并的目录
result_dir = './MERGE_RESULT'       # 合并完成的目录

# gci(to_merge_dir)
# print(mydict)

fileTypes = get_file_names(to_merge_dir)
print(fileTypes)