l1 = list()
l2 = list()
with open("input.txt", 'r', encoding='utf-8') as f:
	for line in f:
		first, *_, second = line.split()
		l1.append(int(first))
		l2.append(int(second))
l1.sort()
l2.sort()
print(sum(abs(a - b) for a, b in zip(l1, l2)))
