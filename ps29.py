import itertools 
import numpy

#some cool code I realised isn't actually necessary for this problem, but still cool

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
    
def element_counter(list):
	'''
	returns dictionary of frequency (value) of element (key) in list
	'''
	dictionary={}
	while len(list)>0:
		value=list.count(list[0])
		key=list[0]
		dictionary[key]= value
		list=[x for x in list if x != list[0]]
	return dictionary

#actual useful code start here

def distinct_powers(upto):
	combos= list(itertools.combinations_with_replacement(range(2,upto+1), 2))
	print combos
	distinct_powers=set()
	for i in range(0,len(combos)):
		tuple=combos[i]
		power=[tuple[0]**tuple[1]]
		distinct_powers.update(power)
		power=[tuple[1]**tuple[0]]
		distinct_powers.update(power)
	print distinct_powers
	return len(distinct_powers)

print distinct_powers(100)













