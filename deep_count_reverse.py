def is_list(p):
	return isinstance(p,list)

def deep_count(p):
	sum = 0
	for e in p:
		sum = sum + 1
		if is_list(e):
			sum = sum + deep_count(e)
	return sum		

def deep_reverse(p):
	if is_list(p):
		result = []
		for i in range(len(p) - 1, -1, -1):
			result.append(deep_reverse(p[i]))
		return result	
	else:
		return p	


print(deep_count([1,[],[2,[3]]]))	
print(deep_reverse([1,[],[2,[3,4,5]]]))