import collections
def alphabetic_names(inputfile):
	''' 
	inputfile is name of file
	alphabet is a string of the alphabet
	'''
	names = open(inputfile, 'r').read() #list of names as strings
	namessorted=sorted(names.split(','))
	for i in range(0, len(namessorted)):
		namessorted[i]=namessorted[i].strip('"')
	return namessorted

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_number(alphabet):
	alphabetnums={}
	for i in range(1,27):
		letter=alphabet[i-1:i]
		alphabetnums[letter]= i
	return alphabetnums

def name_score(inputfile, alphabet):
	namelist=alphabetic_names(inputfile) #list of names in alphabetical order
	alphanums=alphabet_number(alphabet) #dictionary pairing letters to their score
	scoredict={}
	for i in range(0,len(namelist)):
		name=namelist[i]
		score=0
		for j in range(0,len(name)):
			letter=name[j]
			score=score+alphanums[letter]
		scoredict[i]=score 
	totalscore=0
	for i in range(0, len(namelist)):
		totalscore=totalscore+(i+1)*scoredict[i]
	return totalscore 


print name_score("p022_names.txt", alphabet)
