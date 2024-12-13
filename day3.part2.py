with open("input.txt", 'r', encoding='utf-8') as f:
	content = f.read()
first, *rest_dont_splits = content.split("don't()")
filtered = first
for dont_split in rest_dont_splits:
	if (do_idx := dont_split.find("do()")) != -1:
		filtered += dont_split[do_idx:]
from re import findall
mul_pat = r"mul\((\d+),(\d+)\)"
print(sum(int(a) * int(b) for a, b in findall(mul_pat, filtered)))
