import math
import collections

def prime_numbers(upto):
	leftover= collections.OrderedDict()
	for i in range(2,upto):
		leftover[i] = i
	num=2
	prime=[]
	while num<= math.ceil(math.sqrt(upto))+1:
		for i in range(num*2,upto,num):
			try:
				del leftover[i]
			except KeyError:
				pass
		if leftover.values()[0]==num:
			prime.append(num)
			del leftover[num]
		num=leftover.values()[0]
	leftover=list(leftover.values())
	prime=prime+leftover
	return prime


def largest_prime_factor(num,guess):
	y=True
	x=prime_numbers(guess)
	x.reverse()
	while y==True:
		for i in x:
			if num%i==0:
				return i



print largest_prime_factor(600851475143, 100000)
