# O(nlog(n)) time | O(1) space
def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key = lambda x: x[0])
	mergedIntervals = []
	currentInterval = sortedIntervals[0]
	mergedIntervals.append(currentInterval)
	
	for nextInterval in sortedIntervals:
		# decompose the current interval end, and next interval start and end.
		_, currentIntervalEnd = currentInterval
		nextIntervalStart, nextIntervalEnd = nextInterval
		
		# if there is overlap
		if currentIntervalEnd >=nextIntervalStart:
			currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
		else:
			currentInterval = nextInterval
			mergedIntervals.append(currentInterval)
	
    return mergedIntervals