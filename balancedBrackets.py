def balancedBrackets(string):
	opening = '([{'
	closing = ')]}'
	matchingBrackets = {
		')':'(',
		']':'[',
		'}':'{'
	}
	stack = []
	for bracket in string:
		if bracket in opening:
			stack.append(bracket)
		elif bracket in closing:
			if len(stack) == 0:
				return False
			if stack[-1] == matchingBrackets[bracket]:
				stack.pop()
			else:
				return False
	return len(stack) == 0