# Write a program to compute sin x for given x. The user should supply x and a positive integer
# n. We compute the sine of x using the series and the computation should use all terms in the
# series up through the term involving xn
# sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........


def calculate_series(x, n):
	sum = 0
	for i in range(1, n+1):
		if i % 2 == 0:
			sum -= x**(2*i-1)/factorial(2*i-1)
		else:
			sum += x**(2*i-1)/factorial(2*i-1)
	return sum

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

x = int(input('Enter x: '))
n = int(input('Enter a positive integer: '))
print(round(calculate_series(x, n),4))

# Output: Enter x: 30
# Enter a positive integer: 5
# -0.9881
