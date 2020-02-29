#!/usr/bin/env python3
amout = float(input("1"))
inrate = float(input("2"))
period = int(input("time"))
value = 0
year =1
while year <= period:
    value = amout +(inrate * amout)
    print("year{} Rs. {:.2f}".format(year,value))
    amout = value
    year += 1
