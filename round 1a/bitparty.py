import sys
name = "input1"
path = ""

sys.stdin = open(path + name + ".in")
#sys.stdout = open(path + name + ".out", "w")


def find(robots, bits, n, mlst):
    bits2 = list()
    for i in range(n):
        bits2.append([mlst[i][0],mlst[i][0]*mlst[i][1]+mlst[i][2],mlst[i][1]+mlst[i][2]])
    bits2.sort(key=lambda x: (-x[0],x[1],x[2]))
    s = list()
    i = 0
    while bits > 0:
        if bits >= robots:
            s.append(bits2[i][1])
            bits -= bits2[i][0]
            i += 1
        else:
            s.append(bits2[ i ][ 2 ])
            i += 1
            bits -= 1
    return max(s)
if __name__ == "__main__":
    t = int(input())
    for a0 in range(t):
        inp = list(map(int, input().split(' ')))
        mlst = list()
        for i in range(inp[2]):
            lst = list(map(int, input().split(' ')))
            mlst.append(lst)
        print("Case #", a0 + 1, ": ",find(inp[0],inp[1],inp[2],mlst), sep="")