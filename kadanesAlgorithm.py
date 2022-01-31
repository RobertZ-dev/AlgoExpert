def kadanesAlgorithm(array):
	maxSoFar, maxEndingHere = array[0], array[0]	
	for num in array[1:]:
		maxEndingHere = max(maxEndingHere + num, num)
		maxSoFar = max(maxSoFar, maxEndingHere)
	return maxSoFar