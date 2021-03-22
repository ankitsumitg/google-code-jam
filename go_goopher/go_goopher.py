import sys
import random
import math
def solve(d,a):
    coor = math.floor(math.sqrt(a))
    case_done = False
    while case_done == False:
        x, y = map(int, input().split())
        if x == -1 and y == -1:
            print(x, y, sep=' ')
        if x == 0 and y == 0:
            case_done = True
            break

        d[(x,y)] = 1
        x = random.randint(10,10+coor)
        y = random.randint(10,10+coor)
        print(x,y,sep=' ')
        d[ (x, y) ] = 1
        sys.stdout.flush()

t = int(input())
for _ in range(t):
    a = int(input().strip())
    d = dict()
    x = 10
    y = 10
    d[(x,y)] = 1
    print(x, y, sep=' ')
    sys.stdout.flush()
    solve(d,a)