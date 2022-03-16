# O(nlog(n)) time | O(log(n)) space
# worst O(n^2) time
def quickSort(array):
	qshelper(array, 0, len(array) - 1)
	return array
	
def qshelper(array, startIdx, endIdx):
	if startIdx >= endIdx:
		return
	pivotIdx = startIdx 
	leftIdx = startIdx + 1
	rightIdx = endIdx
	while rightIdx >= leftIdx:
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1
	# after the while loop terminates, rightIdx is on the left of leftIdx, swap rightIdx
	# and pivotIdx elements:
	array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]
	leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
	if leftSubarrayIsSmaller:
		qshelper(array, startIdx, rightIdx - 1)
		qshelper(array, rightIdx + 1, endIdx)
	else: 
		qshelper(array, rightIdx + 1, endIdx)
		qshelper(array, startIdx, rightIdx - 1)