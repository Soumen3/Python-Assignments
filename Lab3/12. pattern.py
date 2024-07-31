# Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125


def print_table():
	for i in range(1, 6):
		print(i,1, end=' ')
		for j in range(1, 4):
			print(i**j, end=' ')
		print()

print_table()