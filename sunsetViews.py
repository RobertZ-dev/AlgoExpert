# O(n) time | O(n) space
def sunsetViews(buildings, direction):
	candidateBldgs = []
	startIdx = 0 if direction == "EAST" else len(buildings) - 1
	step = 1 if direction == "EAST" else -1
	idx = startIdx
	while idx >= 0 and idx < len(buildings):
		buildingHeight = buildings[idx]
		while len(candidateBldgs) > 0 and buildings[candidateBldgs[-1]] <= buildingHeight:
			candidateBldgs.pop()
		candidateBldgs.append(idx)
		idx += step
	if direction == "WEST": 
		return candidateBldgs[::-1]
	return candidateBldgs
