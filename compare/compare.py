#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 整体策略说明
# - 对同一语言，从本地各仓库获取最新 merge 的项目为 v1.json，从 crowdIn 中获取的项目
# 为 v2
# - 序列化 v1.json 和 v2.json
# - 以 v1.json 作为基础，比较 v1.json 和 v2.json,
#     * 改动的：使用 v2 文件
#     * 相同的：跳过
#     * 新增的：跳过
# - 获取新的结果 result，并进行反序列化
# - 将反序列化的内容，输出到文件中，作为该翻译语种的最终版本 result.json

import serialize as sl

v1 = sl.serialize('v1.json')
v2 = sl.serialize('v2.json')
result = sl.deserialize(sl.compare(v1, v2))
sl.write_to_file('./result.json', result)
