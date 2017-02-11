def MaxTrianglePath():
	triangle={}
	text = open('triangle.txt','r')
	i=1
	for line in text.read().split('\n'):
		line=line.split()
		for j in range(0,i):
			triangle[(i,j+1)]= int(line[j])
		i=i+1
	size=i
	r=range(2,size)
	r.reverse()
	print "triangle", triangle 
	for i in r:
		for j in range(1,i):
			triangle[(i-1,j)]=triangle[(i-1,j)]+max(triangle[(i,j)], triangle[(i,j+1)])
			print "index %r %r" %(i-1,j)
			print "triangle piece", triangle[(i-1,j)] 
	return triangle[(i-1, i-1)]

print MaxTrianglePath()

