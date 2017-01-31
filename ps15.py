def lattice_path(gridsize):
	lattice={}
	for i in range(0,gridsize+1):
		for j in range(0,gridsize+1):
			lattice[(0,j)]=1
			lattice[(i,0)]=1
	for i in range(1,gridsize+1):
		for j in range(1,gridsize+1):
			lattice[(i,j)]=lattice[(i-1,j)]+lattice[(i,j-1)]
	return lattice 

print lattice_path(20)[(20,20)]