import sys

name = "input1"
path = ""

sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")
def solve(n, l, w):
    used = set([''])
    for i in range(l):
        ls = set(x[i] for x in w)
        nu = set()
        for x in w:
            nu.add(x[:i + 1])
        for s in used:
            for c in ls:
                ss = s + c
                if ss not in nu:
                    return ss + w[0][i + 1:]
        used = nu
    return '-'


for t in range(1, int(input()) + 1):
    n, l = map(int, input().split())
    w = [input() for x in range(n)]
    print('Case #%d:' % t, solve(n, l, w))