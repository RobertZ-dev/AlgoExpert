# O(n) time | O(1) space
def validStartingCity(distances, fuel, mpg):
	numberOfCities = len(distances)
	milesRemaining = 0
	
	startCityCandidate, milesRemainingAtStartCityCandidate = 0, 0
	for cityIdx in range(1, numberOfCities):
		distanceFromPreviousCity = distances[cityIdx - 1]
		fuelFromPreviousCity = fuel[cityIdx - 1]
		milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity
		
		if milesRemaining < milesRemainingAtStartCityCandidate:
			milesRemainingAtStartCityCandidate = milesRemaining
			startCityCandidate = cityIdx
	return startCityCandidate