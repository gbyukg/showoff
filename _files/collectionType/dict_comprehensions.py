#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# 列出当前文件所在目录下的所有文件的大小
# os.listdir() 返回指定目录下的文件列表
# os.path.isfile 判断是否是文件
file_size = {name: os.path.getsize(name) for name in os.listdir('.') if os.path.isfile(name)}
print(file_size)
