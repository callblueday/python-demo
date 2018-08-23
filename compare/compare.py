#!/usr/bin/python
# -*- coding: UTF-8 -*-

# https://github.com/mewwts/addict

import json
import os
from addict import Dict

def loadJson():
    f = open("v1.json")
    content = json.load(f)
    # content = Dict(content)
    return content;



t = loadJson()

print(t.has_key('order_change'))
print(t.has_key('mscratch-i18n/msg'))


# t['mscratch-i18n/msg']['blocks]
# print(t['mscratch-i18n/msg']['blocks'])

# 打开 v2.json，抽离成字典，用于做对比

# 打开 v1.json，逐行读取文件

# 写入到新文件 v3.json
