# O(n*2^n) space | O(n*2^n) time
def powerset(array):
	subsets = [[]]
	for num in array: 
		for i in range(len(subsets)):
			currentSubsets = subsets[i]
			subsets.append(currentSubsets + [num])
	return subsets