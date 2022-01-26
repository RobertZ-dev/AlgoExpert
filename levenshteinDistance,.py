# O(nm) time | O(min(n, m)) space
def levenshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
	big = str1 if len(str1) >= len(str2) else str2
	evenRow = [x for x in range(len(small) + 1)]
	oddRow = [None for x in range(len(small) + 1)]
	for i in range(1, len(big) + 1):
		if i % 2 == 1:
			currentRow = oddRow
			previousRow = evenRow
		else:
			currentRow = evenRow
			previousRow = oddRow
		currentRow[0] = i
		for j in range(1, len(small) + 1):
			if big[i - 1] == small[j - 1]:
				currentRow[j] = previousRow[j - 1]
			else:
				currentRow[j] = 1 + min(previousRow[j -1], previousRow[j], currentRow[j-1])
	return evenRow[-1] if len(big) % 2 == 0 else oddRow[-1]