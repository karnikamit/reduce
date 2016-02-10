# -*- coding: utf-8 -*-
__author__ = "karnikamit"

# find the sum of numbers

a_list = range(100)
print reduce(lambda x, y: x + y, a_list)

# find the greatest no

b_list = [1, 2, 4, 3, 10, 100]
print reduce(lambda x, y: x if x > y else y, b_list)
