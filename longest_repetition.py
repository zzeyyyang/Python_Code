def longest_repetition(input_list):
	best_element = None
	length = 0
	current = None
	current_length = 0
	for element in input_list:
		if current != element:
			current = element
			current_length = 1
		else:
			current_length += 1
		if current_length > length:
			best_element = current
			length = current_length
	return best_element


print(longest_repetition([7,6,6,5,5,5,6,6,7]))					