# O(2n)~O(n) time | O(n) space
def arrayOfProducts(array):
	products = [1 for _ in range(len(array))]
	leftRunningProduct = 1
	for left in range(len(array)):
		products[left] = leftRunningProduct
		leftRunningProduct *= array[left]
		
	rightRunningProduct = 1
	for i in reversed(range(len(array))):
		products[i] *= rightRunningProduct
		rightRunningProduct *= array[i]
	return products