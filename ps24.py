def lexico_permute(location):
	permutation={}
	for i in range(10):
		permutation[i+1]=itertools.permutation(i+1)
