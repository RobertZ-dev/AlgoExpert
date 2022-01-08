# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
	i, j = 0, 0
	while i <= (len(array) - 1):
		if array[i] == toMove:
			i += 1
		else:
			array[j], array[i] = array[i], array[j]
			i += 1
			j += 1
	return array