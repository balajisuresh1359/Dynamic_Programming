import time
def fib(n,memo={}):
	if n in memo:
		return memo[n]
	if n<=2:
		return 1
	memo[n] = fib(n-1,memo)+fib(n-2,memo)
	return memo[n]

def fibn(n):
	if n<=2:
		return 1
	return fibn(n-1)+fibn(n-2)


start = time.time()
print(fib(20))
print(str(time.time()-start))

start = time.time()
print(fibn(20))
print(str(time.time()-start))
#1 1 2 3 5 8 13 21 34 55
#1 2 3 4 5 6 7  8  9  10
