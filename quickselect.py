# O(n) time | O(1) space
def quickselect(array, k):
	position = k - 1
	return quickselectHelper(array, 0, len(array) - 1, position)

def quickselectHelper(array, startIdx, endIdx, position):
	while True:
		if startIdx > endIdx:
			raise Exception("Your algorithm should never arrive here!")
		pivotIdx = startIdx
		leftIdx = startIdx + 1
		rightIdx = endIdx
		while leftIdx <= rightIdx:
			if array[leftIdx] > array[pivotIdx] > array[rightIdx]:
				array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
			if array[leftIdx] <= array[pivotIdx]:
				leftIdx += 1
			if array[rightIdx] >= array[pivotIdx]:
				rightIdx -= 1
		array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]
		if rightIdx == position:
			return array[rightIdx]
		elif rightIdx < position:
			startIdx = rightIdx + 1
		else:
			endIdx = rightIdx - 1