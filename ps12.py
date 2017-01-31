def number_of_divisors(n):
'''
this function returns the number of factors of any number n
it does so by striping n of its prime factors from smallest to biggest 
this method relies on the number in question not having a single huge prime factor
you would hope that is the case for the *smallest* number to have 500 (i.e. a lot of) factors
'''
    if n % 2 == 0: n = n/2 #consider first the number of factors equal to 2 of n
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
	#then consider all its odd prime factors
    p = 3
    while n != 1: #stop once number has been stripped clean 
        count = 0
        #keep removing prime factors of the same number until no longer divisible by that number
        #note the next line is always FALSE for any p that is composite
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1) #the number of divisors is equal to the product of the exponent on prime factors
        p += 2
    return divisors


def trianglefactors(upto):
#gives triangle number with at least upto factors
	n=1
	ndiv, n1div = number_of_divisors(n), number_of_divisors(n+1)
	'''
	the total number of divisors of a triangle number is equal to the number of divisors of n
	times the number of divisors of n+1. We don't have to worry about the two numbers sharing divisors
	because any number is uniquely defined by its prime factors and n and n+1 are coprime. 
	'''
	while ndiv*n1div<upto:
		n+=1
		ndiv, n1div= n1div, number_of_divisors(n+1)
	return n*(n+1)/2


print trianglefactors(500)  





