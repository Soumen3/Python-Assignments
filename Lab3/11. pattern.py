# Print the pattern upto N lines:
# 1 2
# 4 3

# N=2

# 1 2 3
# 8 9 4
# 7 6 5

# N=3

# 1 2 3 4
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7

# N=4


def print_pattern(n):
	if n < 2:
		print('N should be greater than 1')
		return
	matrix = [[0 for i in range(n)] for j in range(n)]
	i,j = 1, 1
	e = 1
	right = n
	down = n
	left = 0
	up = 1
	while e <= n*n:
		while j <= right:
			matrix[i-1][j-1] = e
			e += 1
			j += 1
		right -= 1
		j -= 1
		i += 1
		while i <= down:
			matrix[i-1][j-1] = e
			e += 1
			i += 1
		down -= 1
		i -= 1
		j -= 1
		
		while j > left:
			matrix[i-1][j-1] = e
			e += 1
			j -= 1
		left += 1
		j += 1
		i -= 1
		while i > up:
			matrix[i-1][j-1] = e
			e += 1
			i -= 1
		up += 1
		i += 1
		j += 1



	for i in range(n):
		for j in range(n):
			print(matrix[i][j], end=' ')
		print()
			


n = int(input('Enter N: '))
print_pattern(n)
