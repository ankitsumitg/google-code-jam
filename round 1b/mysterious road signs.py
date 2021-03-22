import sys

name = "input1"
path = ""

sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")

def get_ints():
    ret = tuple(map(int, input().strip().split()))
    # print(ret)
    return ret

def solve_case(t):
    total= get_ints()[0]
    D = list()
    A = list()
    B = list()
    for i in range(total):
        l = list(get_ints())
        D.append(l[0])
        A.append(l[1])
        B.append(l[2])
    s = list()
    d = list()
    s2 = list()
    d2 = list()
    for i in range(total):
        s.append(D[ i ] + A[ i ])
        d.append(D[ i ] - B[ i ])
    s2 = list(set(s))
    d2 = list(set(d))
    max_len = 0
    count = dict()
    c = 0
    len = 0
    count[len] = 0
    pair = dict()
    ss = ""
    for a in s2:
        for b in d2:
            for i in range(total):
                if a == s[i] or b == d[i]:
                    len += 1
                    ss += str(i)

                else:
                    if len > max_len:
                        max_len = len
                        count[max_len] = 1
                    elif len == max_len:
                        if not ss in pair:
                            pair[ss] = True
                            count[max_len] += 1
                    c = 0
                    len = 0
                    ss = ""
            if len>0:
                if len > max_len:
                    max_len = len
                    count[ max_len ] = 1
                elif len == max_len:
                    if not ss in pair:
                        pair[ ss ] = True
                        count[ max_len ] += 1
            c = 0
            len = 0
            ss = ""
    print("Case #%d: %d %d" % (t,max_len,count[max_len]))


def main():
    t = get_ints()[ 0 ]
    for i in range(1, t + 1):
        solve_case(i)


try:
    main()
except Exception as e:
    print(e)