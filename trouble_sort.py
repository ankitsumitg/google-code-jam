#!/bin/python3

#import sys
import itertools
def reverse_sublist(lst,start,end):
    lst[start:end+1] = lst[start:end+1][::-1]
    return lst

def check(l,n):
    for i in range(0,n-1):
        if not l[i] <= l[i+1]:
            return i
    return "OK"

def tsort(lst, n):
    # Complete this function
    done = False
    while not done:
        done = True
        for i in range(0,n-2):
            if lst[i] > lst[i+2]:
                done = False
                #lst = reverse_sublist(lst,i,i+2)
                lst[i],lst[i+2] = lst[i+2],lst[i]
    return check(lst,n)

def tsort_large(lst, n):
    lst1 = list()
    lst2 = list()
    for i in range(0,len(lst)):
        if i%2 == 0:
            lst1.append(lst[i])
        else:
            lst2.append(lst[i])
    lst1.sort()
    lst2.sort()
    old = lst1[0]
    index = -1
    l = [iter(lst1),iter(lst2)]
    for i in itertools.cycle(l):
        try:
            new = i.__next__()
            if old >= new and index>-1:
                return index
            old = new
            index += 1
        except:
            StopIteration
            break
    return "OK"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        lst = list(map(int, input().strip().split(' ')))
        #print("Case #",a0+1,": ",tsort(lst,n),sep="")
        print("Case #", a0 + 1, ": ", tsort_large(lst, n), sep="")