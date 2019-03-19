def  number_in_lists(string):
	n = len(string)
	out = []
	i = 0
	while i < n:
		sub = []
		out.append(int(string[i]))
		j = i + 1
		while j < n and string[j] <= string[i]:
			sub.append(string[j])
			j = j + 1
		if sub:
			out.append(sub)
		i = j
	return out		

a = '996'
print(number_in_lists(a))
	