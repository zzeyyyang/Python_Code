def check_sudoku(p):
	n = len(p)
	digit = 1
	while digit <= n:
		i = 0
		while i < n:
			row_count = 0
			col_count = 0
			j = 0
			while j < n:
				if p[i][j] == digit:
					row_count = row_count + 1
				if p[j][i] == digit:
					col_count = col_count + 1
				j = j + 1
			if row_count != 1 or col_count != 1:
				return False
			i = i + 1
		digit = digit + 1
	return True						