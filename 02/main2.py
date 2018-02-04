# coding: utf-8
from functools import reduce

target1 = 'パトカー'
target2 = 'タクシー'
result = ''.join(reduce(lambda x, y: x + y, zip(target1, target2)))
print(result)
