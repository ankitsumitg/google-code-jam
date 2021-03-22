import sys

name = "input1"
path = ""

sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")
def solve(arr):
    arr = arr[::-1]
    # print arr
    dp = [0]
    for w in reversed(arr):
        lim = 6*w
        for ln, wsum in reversed(list(enumerate(dp))):
            if wsum > lim:
                continue
            if ln + 1 >= len(dp):
                dp.append(wsum + w)
            else:
                dp[ln+1] = min(dp[ln+1], wsum + w)
    # print dp
    return len(dp) - 1



tn = int(input())
for ti in range(tn):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = solve(arr)
    print("Case #%d: %s" % (ti+1, ans))