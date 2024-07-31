# Declare a function named reverse_list. It takes an array as a parameter and it returns the
# reverse of the array (use loops).

def reverse_list(lst):
	rev = []
	for i in range(-1, -len(lst), -1):
		rev.append(lst[i])
	return rev

lst = [eval(e) for e in input('Enter a list of numbers separated by space: ').split()]
print(reverse_list(lst))