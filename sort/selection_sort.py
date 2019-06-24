import sys

unsorted = list(map(int, input().split()))

bsorted = unsorted[:]

for i in range(0, len(bsorted)):
	min_v = sys.maxsize
	for j in range(i, len(bsorted)):
		if bsorted[j] < min_v:
			min_v = bsorted[j]
			min_idx = j

	if min_idx != i:
		bsorted[min_idx] = bsorted[i]
		bsorted[i] = min_v

			
print(bsorted)

if all(list(map(lambda t : t[0] == t[1], zip(bsorted, sorted(unsorted))))):
	print("OK")
else:
	print("ERROR")
