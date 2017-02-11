import collections

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_number(alphabet):
	alphabetnums={}
	for i in range(10,36):
		letter=alphabet[i-10:i-9]
		alphabetnums[letter]= str(i)
	return alphabetnums

def alphabetic(inputfile, alphabet):
	''' 
	inputfile is name of file
	alphabet is a string of the alphabet
	'''
	names = open(inputfile, 'r').read() #list of names as strings
	nameslist=names.split(',')
	for i in range(0, len(nameslist)):
		nameslist[i]=nameslist[i].strip('"')
	alphanums=alphabet_number(alphabet) #dictionary paring letters to numbers based on size  
	namedict={}
	for i in range(0, len(nameslist)):
		namenumber=""
		j=0
		while j<=(len(nameslist[i])-1):
			temp=nameslist[i]
			print "temp", temp 			
			namenumber=namenumber+alphanums[temp[j]]
			j=j+1
			print j
		namedict[namenumber]=temp 
	orderednamedict=collections.OrderedDict(namedict)
	return orderednamedict 





print alphabetic("p022_names.txt", alphabet)
#print alphabet_number(alphabet)
