def fib(end):
	if end > 2:
		fib = [0,1]
		for i in range(1,end):
			fib.append(fib[i]+fib[i-1])
	
		print("These are the first {0} fibonanci numbers".format(end))
		print(fib)
	else:
		print("%d is not greater than 2" % (end))
