import itertools 
import numpy
def prime_divisors(n):
    '''
    this function returns all prime factors of number n (with repeats)
    it does so by striping n of its prime factors from smallest to biggest 
    this method relies on the number in question not having a single huge prime factor
    '''
    factors=[]
    while n % 2 == 0:
        factors.append(2)
        n = n/2
	#then consider all its odd prime factors
    p = 3
    while n != 1: #stop once number has been stripped clean 
        #keep removing prime factors of the same number until no longer divisible by that number
        while n % p == 0:
            factors.append(p)
            n = n/p
        p=p+1
    return factors

def sum_all_divisors(n):
    '''
    function returns SUM of all divisors (excluding n) of the number n
    '''
    all_factors=set()
    repeat_prime=prime_divisors(n)
    for i in range(1,len(repeat_prime)+1): 
    #key is to notice that the product of all combinations of prime divisors gives all factors
        factor_decomposition=list(itertools.combinations(repeat_prime,i))
        for j in range(0,len(factor_decomposition)):
            all_factors.add(numpy.prod(factor_decomposition[j]))
    all_factors=list(all_factors)
    all_factors.remove(n)
    all_factors.append(1)
    total=sum(all_factors)
    return total

def amicable(upto):
    '''
    find amicable pairs, where sum of proper divisors equals other in amicable pairs
    '''
    numsum={}
    amicablepair=set()
    for i in range(2,upto+1):
        numsum[i]=sum_all_divisors(i) #key to numsum dictionary is number, value is sum of factors
    print numsum
    for i in range(2,upto+1):
        try:
            if numsum[numsum[i]]==i and numsum[i]!=i: #avoid numbers with factor sum equal to itself
                amicablepair.update([i, numsum[i]])
        except KeyError:
            pass 
    return amicablepair 

print sum(list(amicable(10000)))
