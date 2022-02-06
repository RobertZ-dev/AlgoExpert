def taskAssignment(k, tasks):
	sort_tasks = sorted(tasks)
	pairedTasks = []
	left, right = 0, len(sort_tasks) - 1
	while left < right:
		pairedTasks.append([tasks.index(sort_tasks[left]), tasks.index(sort_tasks[right])])
		tasks[tasks.index(sort_tasks[left])] = 0
		tasks[tasks.index(sort_tasks[right])] = 0
		left += 1
		right -= 1
	return pairedTasks