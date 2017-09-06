#!/usr/bin/env python
# -*- coding: utf-8 -*-

def outer_func():
    message = 'Hi'

    def inner_func():
        nonlocal message
        message = 'Hello'
        print(message)

    result = inner_func()
    print(message)
    return result

outer_func()
