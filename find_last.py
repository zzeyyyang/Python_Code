def find_last(s,t):
	last_pos = -1
	while True:
		pos = s.find(t,last_pos + 1)
		if pos == -1:
			return last_pos
		last_pos = pos	