# O(m*n) time | O(min(m,n)) space
def numberOfWaysToTraverseGraph(width, height):
	small = width if width < height else height
	big = width if width >= height else height
	evenRow = [ 1 for _ in range(small) ]
	oddRow = [1 for _ in range(small)]
	for i in range(1, big):
		if i % 2 == 1:
			currentRow = oddRow
			previousRow = evenRow
		else:
			currentRow = evenRow
			previousRow = oddRow
		currentRow[0] = 1
		for j in range(1, small):
			currentRow[j] = previousRow[j] + currentRow[j-1]
	return currentRow[-1]