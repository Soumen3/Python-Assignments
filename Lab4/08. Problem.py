# Please write a program which count and print the numbers of each character in a string input by console.
# Example:
# If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

string = input("Enter a string: ")
characters = {}
for char in string:
	if char in characters:
		characters[char] += 1
	else:
		characters[char] = 1

for char, count in characters.items():
	print(f"{char},{count}")
