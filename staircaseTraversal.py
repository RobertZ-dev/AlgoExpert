# O(k*n) time | O(n) space
def staircaseTraversal(height, maxSteps):
	NumOfWays = [0 for _ in range(height+1)]
	NumOfWays[0], NumOfWays[1] = 1, 1
	for idx in range(2, height+1):
		for i in range(1, maxSteps + 1):
			NumOfWays[idx] += NumOfWays[idx - i]
	return NumOfWays[-1]
