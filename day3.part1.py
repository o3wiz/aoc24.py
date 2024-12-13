with open("input.txt", 'r', encoding='utf-8') as f:
	content = f.read()
from re import findall
mul_pattern = r'mul\((?P<a>\d+),(?P<b>\d+)\)'
print(sum(int(a) * int(b) for a, b in findall(mul_pattern, content)))
