import numpy as np

def longest_Collatz(upto):
	remaining= set(range(1,upto+1))
	nodes=set(range(1,upto+1))
	even=set(range(2,100000,2))
	odd=set(range(1,100000,2))
	while len(remaining)>1:
		evennodes= nodes-odd
		print "even nodes", evennodes
		oddnodes=nodes-even
		print "odd nodes", oddnodes
		toremoveeven= set(0.5*np.array(list(evennodes)))
		print "to remove from even", toremoveeven 
		toremoveodd= set(3*(np.array(list(oddnodes)))+1)
		print "to remove from odd", toremoveodd
		nodes=set(toremoveeven.union(toremoveodd)-remaining)
		remaining=remaining-toremoveeven-toremoveodd
		print "remaining", remaining
		raw_input("press enter to continue")
	return remaining

print longest_Collatz(100)