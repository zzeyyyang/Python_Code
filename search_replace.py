def make_converter(match, replacement):
	return [match, replacement]

def apply_converter(converter, string):
	previous = None
	while previous != string:
		previous = string
		position = string.find(converter[0])	
		if position != -1:
			string = string[:position] + converter[1] + string[position + len(converter[0]):]
	return string
	



def search_replace(converter, string):
	position = string.find(converter[0])
	if position == -1:
		return string
	else:
		string = string[:position] + converter[1] + string[position + len(converter[0]):]
		return search_replace(converter, string)



converter = make_converter('aba','a')
print(apply_converter(converter, 'ababa'))
print(search_replace(converter, 'ababa'))