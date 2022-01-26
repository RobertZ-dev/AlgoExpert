def minNumberOfCoinsForChange(n, denoms):
	numOfCoin = [float('inf') for amount in range(n+1)]
	numOfCoin[0] = 0
	for denom in denoms:
		for amount in range(1, n+1):
			if denom <= amount:
				numOfCoin[amount] = min(numOfCoin[amount], 1 + numOfCoin[amount - denom])
	return numOfCoin[-1] if numOfCoin[-1] != float('inf') else -1