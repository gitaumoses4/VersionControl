def fib(end):
	if end > 2:
		fib = [0,1]
		for i in range(1,end-1):
			fib.append(fib[i]+fib[i-1])

		return fib
	else:
		return "{0} is not greater than 2".format(end)
