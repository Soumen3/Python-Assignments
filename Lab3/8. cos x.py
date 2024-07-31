# Write a program to compute cosine of x. The user should supply x and a positive integer n.
# We compute the cosine of x using the series and the computation should use all terms in the
# series up through the term involving xn
# cos x = 1 - x2/2! + x4/4! - x6/6! ....


def calculate_series(x, n):
	sum = 0
	for i in range(1, n+1):
		if i % 2 == 0:
			sum += x**(2*i)/factorial(2*i)
		else:
			sum -= x**(2*i)/factorial(2*i)
	return sum

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

x = int(input('Enter x: '))
n = int(input('Enter a positive integer: '))

print(round(calculate_series(x, n),4))
