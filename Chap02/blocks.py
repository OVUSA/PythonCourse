#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73
x = x + y

if x == y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x < y:
    print('x > y: x is {} and y is {}'.format(x, y))
elif x == 115:
    print('x is {}'.format(x))
else:
    print('x is {}'.format(x))
