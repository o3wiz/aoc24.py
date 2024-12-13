l1 = list()
l2 = list()
with open("input.txt", 'r', encoding='utf-8') as f:
	for line in f:
		first, *_, second = line.split()
		l1.append(int(first))
		l2.append(int(second))

from collections import Counter
second_list_freqs = Counter(l2)
print(sum(a * second_list_freqs.get(a, 0) for a in l1))
