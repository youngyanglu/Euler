def fibonaccisum(limit):
	seed=1
	number=2
	total=0
	while number < limit:
		if number %2 == 0:
			print "the number is", number/2 
			total=total+number 
			print "the total now is", total
		else:
			pass 
		newnumber=number+seed
		seed=number 
		number=newnumber 
	return total

#set upper limit of sequence
limit=4000000

print "the sum is", fibonaccisum(limit)