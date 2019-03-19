def symmetric(A):
	n = len(A)
	for e in A:
		if len(e) != n:
			return False
	i = 0
	while i < n:
		j = 0
		while j < n:
			if A[i][j] != A[j][i]:
				return False
			j = j + 1
		i = i + 1
	return True									