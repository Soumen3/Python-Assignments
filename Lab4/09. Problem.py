# 9.Write a program that accepts a string
# I. 1.reverses it.
# II. 2.checks whether it is a palindrome.
# III. 3.checks whether it ends with a specific substring.
# IV. 4.capitalize the first letter of each word in a string
# V. 5.check if a string is anagram of another string
# VI. 6.remove vowels from string
# VII. 7.find length of the longest word in a sentence


# I. 1.reverses it.
string = input("Enter a string: ")
print(string[::-1])

# II. 2.checks whether it is a palindrome.
string = input("Enter a string: ")
if string == string[::-1]:
	print("Palindrome")
else:
	print("Not a palindrome")

# III. 3.checks whether it ends with a specific substring.
string = input("Enter a string: ")
substring = input("Enter a substring: ")
if string.endswith(substring):
	print("Yes")
else:
	print("No")

# IV. 4.capitalize the first letter of each word in a string
string = input("Enter a string: ")
words = string.split()
words = [word.capitalize() for word in words]
print(" ".join(words))

# V. 5.check if a string is anagram of another string
string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
if sorted(string1) == sorted(string2):
	print("Anagram")
else:
	print("Not an anagram")

# VI. 6.remove vowels from string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
string = "".join([char for char in string if char not in vowels])
print(string)

# VII. 7.find length of the longest word in a sentence
string = input("Enter a string: ")
words = string.split()
lengths = [len(word) for word in words]
print(max(lengths))
