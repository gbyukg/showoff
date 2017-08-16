#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

Sale = collections.namedtuple(
    'Sale',
    'productid customerid date quantity price'
)

s1 = Sale(432, 921, "2017-01-01", 3, 7.99)
s2 = Sale(productid=432, customerid=921, date='2017-01-01', quantity=3, price=7.99)

import pdb; pdb.set_trace()  # XXX BREAKPOINT
print(s1.productid)
import pdb; pdb.set_trace()  # XXX BREAKPOINT
print(s2.date)

print(s1._fields)
print(Sale._fields)

directory_val = s1._asdict()
print(directory_val['date'])
