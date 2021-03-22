def get_ints():
	ret = tuple(map(int, input().strip().split()))
	# print(ret)
	return ret
 
def solve_case(t):
	r, b, c = get_ints()
	M, S, P = [], [], []
	for i in range(c):
		x, y, z = get_ints()
		M.append(x)
		S.append(y)
		P.append(z)
 
	lo = -1
	hi = 2 ** 100 - 1
	while lo < hi - 1:
		mid = (lo + hi) // 2
		bits = 0
		amts = []
		for m, s, p in zip(M, S, P):
			amt = min(m, max(mid - p, 0) // s)
			amts.append(amt)
		amts.sort()
		# print(amts)
		bits = sum(amts[-min(r, c):])
		if bits < b:
			lo = mid
		else:
			hi = mid
	print("Case #%d: %d" % (t, hi))
 
def main():
	t = get_ints()[0]
	for i in range(1, t + 1):
		solve_case(i)
try:
	main()
except Exception as e:
	print(e)