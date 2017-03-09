import time

def longest_Collatz(upto):
	chainlength={}
	chainlength[1]=1
	chainlength[0]=1
	numbers=range(2,upto)

	while len(numbers)>0:
		keyerror=True 
		for i in numbers:
			somenumbers=[] #list of values that return keyerror down the chain of i
			while keyerror==True:
				if i%2==0: #if even
					j=i/2 #what is the next number in the sequence?
				else:
					j=3*i+1 
				try: 
					chainlength[i]=chainlength[j]+1 #then length of i's sequence is one more than j
					if i in numbers: numbers.remove(i) #once added length to dictionary, remove from numbers still to consider
					keyerror=False
				except KeyError: #if j's length isn't known yet, add to numbers if not in numbers
					somenumbers.append(j) 
					i=j
			somenumbers.reverse()
			for i in somenumbers:
				if i%2==0: #if even
					j=i/2 #what is the next number in the sequence?
				else:
					j=3*i+1 
				chainlength[i]=chainlength[j]+1 
				if i in numbers: numbers.remove(i) 
	#remove numbers in dictionary above our upto limit:	
	keys=chainlength.keys()
	for i in keys:
		if i>upto:
			del chainlength[i]
	#Find number with longest chain
	maxlength=max(chainlength.values())
	for number, length in chainlength.iteritems():
	    if length == maxlength:
	    	return number 

start_time = time.time()
print longest_Collatz(1000)
print("--- %s seconds ---" % (time.time() - start_time))