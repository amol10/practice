from copy import copy

unsorted = list(map(int, input().split()))

bsorted = copy(unsorted)


def qsort(arr, start, end):
	if start >= end:
		return

	pivot_idx = partition(arr, start, end)

	qsort(arr, start, pivot_idx - 1)
	qsort(arr, pivot_idx + 1, end)


def partition(arr, start, end):
	pivot_idx = start + int((end - start + 1) / 2)
	pivot = arr[pivot_idx]

	lesser = []
	greater = []

	for i in range(start, end + 1):
		if i == pivot_idx:
			continue

		if arr[i] <= pivot:
			lesser.append(arr[i])
		else:
			greater.append(arr[i])

	new_range = lesser + [pivot] + greater
	for i, new in zip(range(start, end + 1), new_range):
		arr[i] = new
	
	return start + len(lesser)


qsort(bsorted, 0, len(unsorted) - 1)
print(bsorted)

if all(list(map(lambda t : t[0] == t[1], zip(bsorted, sorted(unsorted))))):
	print("OK")
else:
	print("ERROR")
