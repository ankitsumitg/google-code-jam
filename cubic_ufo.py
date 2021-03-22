#!/bin/python3

#import sys
import math
"""
cos(x) = b/h
1
1.414213
"""
def coor(n):
    # Complete this function'
    compute = 2 - n**2
    compute2 = math.sqrt(compute)
    compute3 = (n - compute2) / 2
    """if compute3 < 0:
        compute3 = (n-compute2)/2
    else:
        compute3 = (n + compute2) / 2"""
    a = math.asin(compute3)
    a = -a
    print("Case #", a0 + 1, ": ", sep="")
    x = 0.5
    y = 0
    print(x*math.cos(a) - y*math.sin(a),x*math.sin(a) + y*math.cos(a),0,sep=' ')
    x = 0
    y = 0.5
    print(x*math.cos(a) - y*math.sin(a),x*math.sin(a) + y*math.cos(a),0,sep=' ')
    print(0,0,0.5,sep=' ')

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = float(input().strip())
        coor(n)