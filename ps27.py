def spiral_sum(spiral_size):
	odd_list= [i**2 for i in range(1,spiral_size+2,2)]
	even_list=[i**2+1 for i in range(2,spiral_size+1,2)]
	other_diagonal=[i**2-i+1 for i in range(2,spiral_size+1)]
	total=sum(odd_list)+sum(even_list)+sum(other_diagonal)
	return total

print spiral_sum(1001)