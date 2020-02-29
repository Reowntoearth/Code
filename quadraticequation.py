#!/usr/bin/env python3
import math
a = int(input("1"))
b = int(input("2"))
c = int(input("3"))
d = b * b - 4 * a * c
if d < 0:
    print("have no answer")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b + math.sqrt(d)) / (2 * a)
    print("1:{},2:{}".format(root1,root2))
