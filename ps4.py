def is_palindrome(number):
	numstring=str(number)
	numlist=[numstring[i:i+1] for i in range(0, len(numstring))]
	for i in range(0,len(numlist)/2):
		if numlist[i]!=numlist[len(numlist)-1-i]:
			return False
	return True

def largest_palindrome():
	list=[]
	for num1 in reversed(range(500,999)):
		for num2 in reversed(range (500,999)):
			if is_palindrome(num1*num2):
				list.append(num1*num2)
	return max(list)


print largest_palindrome()
