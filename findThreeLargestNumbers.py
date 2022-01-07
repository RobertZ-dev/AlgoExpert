# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    # Write your code here.
	threeLargest = [None, None, None]
	for num in array:
		updateLargest(threeLargest, num)
	return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)  # TODO
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)  # TODO
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)  # TODO

def shiftAndUpdate(array, num, idx):
	# idx serve the function of shifting depending on what number coming along.
	for i in range(idx + 1):
		if i == idx:
			array[i] = num
		else: 
			array[i] = array[i+1]