# O(n) time | O(1) space
def threeNumberSort(array, order):
	valueCounts = [0, 0, 0]
	for element in array:
		# for each element in the input array, what is its index in the order array
		orderIdx = order.index(element) 
		# find out its corresponding value and start counting in the order counts
		valueCounts[orderIdx] += 1
	
	for i in range(3):
		value = order[i]
		count = valueCounts[i]
		# as i sweeps through 0 to 2, how many value we filled up to order[i]
		numElementsBefore = sum(valueCounts[:i])
		for n in range(count): # start filling up array with order[i] by count times
			currentIdx = numElementsBefore + n # start filling up at numElementBefore + 1 .. count
			array[currentIdx] = value # with the appropriate value
	return array