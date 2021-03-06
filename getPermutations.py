# O(n*n!) time | O(n*n!) space
def getPermutations(array):
	permutations = []
	permutationHelper(0, array, permutations)
	return permutations

def permutationHelper(i, array, permutations):
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		for j in range(i, len(array)):
			# j start with i, first step is a no-op
			swap(array, i, j)
			permutationHelper(i + 1, array, permutations)
			swap(array, i, j)
	return permutations

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]