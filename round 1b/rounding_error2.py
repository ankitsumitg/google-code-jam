def netrem(x, n):
	if 2 * x >= n:
		return n - x
	else:
		return -x

T = int(input())
for case in range(T):
	N, L = map(int, input().split())
	counts = list(map(int, input().split()))
	missing = N - sum(counts)
	remcounts = [netrem((100 * x) % N, N) for x in counts]
	onepersonrem = 100 % N
	#print(remcounts, onepersonrem)
	if onepersonrem == 0:
		print("Case #" + str(case+1) + ":", 100)
		continue
	if onepersonrem * 2 >= N:
		total = sum(remcounts) + missing * (N - onepersonrem)
		print("Case #" + str(case+1) + ":", 100 + total // N)
		continue
	for c in range(N // 2 + 1):
		remcounts.append(0)
	remcounts.sort()
	cur = 0
	remmod = netrem(onepersonrem, N)
	while missing > 0:
		remcounts[cur] += remmod
		missing -= 1
		if remcounts[cur] * 2 <= -N:
			remcounts[cur] += N
			cur += 1
		#print(remcounts)
	total = sum(remcounts)
	print("Case #" + str(case+1) + ":", 100 + total // N)
