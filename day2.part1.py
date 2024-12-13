from itertools import pairwise
ctr = 0
with open("input.txt", 'r', encoding='utf-8') as f:
	for line in f:
		numbers = [int(x) for x in line.split(' ')]
		if (
			all(1 <= a - b <= 3 for a, b in pairwise(numbers))
			or
			all(1 <= b - a <= 3 for a, b in pairwise(numbers))
		):
			ctr += 1
print(ctr)
