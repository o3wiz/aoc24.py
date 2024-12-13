from itertools import pairwise
def is_safe(numbers: list[int]) -> bool:
	return (
		all(1 <= a - b <= 3 for a, b in pairwise(numbers))
		or
		all(1 <= b - a <= 3 for a, b in pairwise(numbers))
	)
ctr = 0
with open("input.txt", 'r', encoding='utf-8') as f:
	for line in f:
		numbers = [int(x) for x in line.split(' ')]
		numbers_with_a_gap = (numbers[:i] + numbers[i + 1:] for i in range(len(numbers)))
		if is_safe(numbers) or any(is_safe(nums) for nums in numbers_with_a_gap):
			ctr += 1
print(ctr)
