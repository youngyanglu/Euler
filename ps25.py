def fibonacci(num_digits):
	n=1
	digits=1
	Fn , Fn_1 = 1 , 1
	while digits<num_digits:
		Fn, Fn_1= Fn_1, Fn_1+Fn
		digits=len(str(Fn_1))
		n=n+1
	return n+1
	
print fibonacci(1000)
