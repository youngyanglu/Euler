import math

def pythagoreantriplet(addition):
	for c in range(addition/3,addition/2):
		b=int((c+(c/math.sqrt(2)))/2)
		y=True
		n=0
		ahatpast=0
		atildepast=0
		while y==True:
			ahat=math.sqrt(c**2-b**2)
			atilde=1000-c-b
			if ahat>atilde and b<c:
				if ahatpast>atildepast or n==0:
					b=b+1 
					ahatpast=ahat
					atildepast=atilde
					n=n+1
				else:
					y=False 
			elif ahat<atilde and b>(c/math.sqrt(2)):
				if ahatpast<atildepast or n==0:
					b=b-1 
					ahatpast=ahat
					atildepast=atilde 
					n=n+1
				else:
					y=False 
			elif ahat==atilde:
				return atilde*b*c
			else:
				y=False 


print pythagoreantriplet(1000)
