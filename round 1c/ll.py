def solve(n):
    sold = [False] * n
    asked = [0] * n
    for i in range(n):
        a = list(map(int, input().split()))[1:]
        ma = n + n
        mx = None
        for x in a:
            asked[x] += 1
            if not sold[x] and asked[x] < ma:
                ma = asked[x]
                mx = x
        if mx is not None:
            sold[mx] = True
            print(mx)
        else:
            print(-1)


for t in range(1, int(input()) + 1):
    solve(int(input()))