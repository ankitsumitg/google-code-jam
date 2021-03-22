# your code goes here
import sys
name = "input1"
path = ""

sys.stdin = open(path + name + ".in")
#sys.stdout = open(path + name + ".out", "w")
def get_ints():
	ret = tuple(map(int, input().strip().split()))
	# print(ret)
	return ret

def solve_case():
	n, p = get_ints()
	baseline = 0
	a = []
	b = []
	for i in range(n):
		w, h = get_ints()
		if w > h:
			w, h = h, w
		a.append(w)
		b.append((w * w + h * h) ** 0.5 - w)
		baseline += w + h
	
	dp = {}
	dp[0] = 0
	for x, y in zip(a, b):
		new_dp = {}
		for i, slack in dp.items():
			new_dp[i] = slack
		for i, slack in dp.items():
			cur_slack = new_dp.get(i + x, -1)
			if y + slack > cur_slack:
				new_dp[i + x] = y + slack
		dp = new_dp
	
	best = baseline
	for i, slack in dp.items():
		if 2 * (i + baseline) <= p:
			best = max(best, min(p, 2 * (i + baseline + slack)))

	return best

def main():
	t = int(input().strip())
	for i in range(1, t + 1):
		s = solve_case()
		print("Case #%d: %.12f" % (i, s))

try:
	main()
except Exception as e:
	print(e)
	
		