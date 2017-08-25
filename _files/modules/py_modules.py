#!/usr/bin/env python
# encoding: utf-8

# 我们还可以在 import 后面使用*来表示引用模块中的所有方法
from requests import get, post
from sys import path

print(path)

# 修改 get->r_get
#response = get('https://api.github.com')
#print(response.text)
