#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    #  raise KeyError
    raise KeyError("key errors") from EnvironmentError
except KeyError as e:
    print(e)

# 第一种语法
