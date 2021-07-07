import time
def fibdp(n,memo={}):
	if n in memo:
		return memo[n]
	if n<=2:
		return 1
	memo[n] = fibdp(n-1,memo)+fibdp(n-2,memo)
	return memo[n]

def fibnormal(n):
	if n<=2:
		return 1
	return fibnormal(n-1)+fibnormal(n-2)


start = time.time()
print(fibnormal(20))
print(str(time.time()-start))

start = time.time()
print(fibdp(20))
print(str(time.time()-start))
#1 1 2 3 5 8 13 21 34 55
#1 2 3 4 5 6 7  8  9  10
