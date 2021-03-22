#!/bin/python3

# import sys
def reverse_sublist(lst, start, end):
    lst[ start:end + 1 ] = lst[ start:end + 1 ][ ::-1 ]
    return lst


def calculate(program):
    initial = 1
    total = 0
    for i in program:
        if i == 'C':
            initial = initial * 2
        else:
            total += initial
    return total


def findnext(program):
    for i in range(len(program) - 1, 0, -1):
        if program[ i ] == 'S' and program[ i - 1 ] == 'C':
            program[ i - 1:i + 1 ] = program[ i - 1:i + 1 ][ ::-1 ]
            return program


def save(damage, program):
    # Complete this function
    c = program.count('S')
    if c > damage:
        return "IMPOSSIBLE"
    if c == 0:
        return 0
    p = list(program)
    c = 0
    while True:
        if calculate(p) <= damage:
            return c
        else:
            for i in range(len(p) - 1, 0, -1):
                if p[ i ] == 'S' and p[ i - 1 ] == 'C':
                    p = reverse_sublist(p, i - 1, i)
                    c += 1
                    break


if __name__ == "__main__":
    t = int(input().strip())
    lst = []
    for a0 in range(t):
        damage, program = input().strip().split(' ')
        damage = int(damage)
        lst.append([damage,program])
    for i in range(len(lst)):
        print("Case #", i + 1, ": ", save(lst[i][0], lst[i][1]), sep="")
