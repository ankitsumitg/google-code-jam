def get_ints():
	ret = tuple(map(int, input().strip().split()))
	# print(ret)
	return ret
 
def converter(c):
	return 1 if c == '@' else 0
 
def solve_case(t):
	r, c, h, v = get_ints()
	grid = []
	for i in range(r):
		grid.append(list(map(converter, input().strip())))
	total_num = sum(map(sum, grid))
 
	if total_num == 0:
		return "POSSIBLE"
	elif total_num % ((h + 1) * (v + 1)):
		return "IMPOSSIBLE"
	else:
		h_cuts = [0]
		cur = 0
		idx = 1
		for i, row in enumerate(grid):
			cur += sum(row)
			if cur > idx * (total_num // (h + 1)):
				return "IMPOSSIBLE"
			elif cur == idx * (total_num // (h + 1)):
				h_cuts.append(i + 1)
				idx += 1
 
		t_grid = list(zip(*grid))
		v_cuts = [0]
		cur = 0
		idx = 1
		for i, row in enumerate(t_grid):
			cur += sum(row)
			if cur > idx * (total_num // (v + 1)):
				return "IMPOSSIBLE"
			elif cur == idx * (total_num // (v + 1)):
				v_cuts.append(i + 1)
				idx += 1
		# print(h_cuts, v_cuts)
		p = total_num // ((h + 1) * (v + 1))
		for i in range(h + 1):
			for j in range(v + 1):
				cur = 0
				for row in range(h_cuts[i], h_cuts[i + 1]):
					cur += sum(grid[row][v_cuts[j]:v_cuts[j + 1]])
				# print(cur, p)
				if cur != p:
					return "IMPOSSIBLE"
		return "POSSIBLE"
 
def main():
	t = int(input().strip())
	for i in range(1, t + 1):
		s = solve_case(i)
		print("Case #%d: %s" % (i, s))
 
try:
	main()
except Exception as e:
	print(e)