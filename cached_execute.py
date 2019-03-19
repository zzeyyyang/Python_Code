def cached_execute(cache,func,inputs):
	if inputs not in cache:
		cache[inputs] = func(inputs)
	return cache[inputs]
	
def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n - 1)			

i = input('Input a number: ')
cache = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
cached_execute(cache,factorial,i)	
print(cache[i])