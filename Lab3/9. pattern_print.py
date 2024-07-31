# Print the pattern upto N Lines (N >=2):

#  .
# /_\
# N=2 
#   .
#  / \
# /___\
# N=3 
#    .
#   / \
#  /   \
# /_____\
# N=4
#     .
#    / \
#   /   \
#  /     \
# /_______\
# N=5




def print_pattern(n):
	if n < 2:
		print('N should be greater than 1')
		return
	for i in range(1, n+1):
		if i == 1:
			print(' '*(n-i) + '.')
		elif i == n:
			print('/' + '_'*(2*n-3) + '\\')
		else:
			print(' '*(n-i) + '/' + ' '*(2*i-3) + '\\')
		


n = int(input('Enter N: '))
print_pattern(n)