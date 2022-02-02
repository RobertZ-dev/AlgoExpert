# O(n) time | O(1) space
def hasSingleCycle(array):
	numElementsVisted = 0 
	currentIdx = 0
	while numElementsVisted < len(array):
		if numElementsVisted > 0 and currentIdx == 0: 
			return False
		numElementsVisted += 1
		currentIdx = getNextIdx(currentIdx, array)
	return currentIdx == 0

def getNextIdx(currentIdx, array):
	jump = array[currentIdx]
	nextIdx = (currentIdx + jump) % len(array)
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)
		