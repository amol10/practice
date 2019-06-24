from copy import copy

unsorted = list(map(int, input().split()))

print(unsorted)
n = len(unsorted)
bsorted = copy(unsorted)

for i in range(n - 1, 0, -1):
	for j in range(0, i):
		if bsorted[j] > bsorted[j + 1]:
			temp = bsorted[j]
			bsorted[j] = bsorted[j + 1]
			bsorted[j + 1] = temp

print(bsorted)

if all(list(map(lambda t : t[0] == t[1], zip(bsorted, sorted(unsorted))))):
	print("OK")

