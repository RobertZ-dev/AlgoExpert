def spiralTraverse(array):
    result = []
	spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
	return result

def spiralFill(array, startRow, endRow, startCol, endCol, result):
	if startRow > endRow or startCol > endCol:
		return
	
	for col in range(startCol, endCol + 1):  # traverse top perimeter
		result.append(array[startRow][col])
		
	for row in range(startRow + 1, endRow + 1): # traverse right perimeter
		result.append(array[row][endCol])
		
	for col in reversed(range(startCol, endCol)): # traverse bottom perimeter
		if startRow == endRow:  # handle edge case when startRow == endRow terminate traverse
			break
		result.append(array[endRow][col])
		
	for row in reversed(range(startRow + 1, endRow)): # traverse left perimeter
		if startCol == endCol: # handle edge case when startCol == endCol terminate traverse
			break
		result.append(array[row][startCol])
	
	spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)