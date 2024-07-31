# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which
# calculates solution set of a quadratic equation, _solve_quadratic_eqn_.

def solve_quadratic_eqn(a, b, c):
	d = b**2 - 4*a*c
	if d < 0:
		return 'No real roots'
	elif d == 0:
		return 'One real root: ', -b / (2*a)
	else:
		return 'Two real roots: ', (-b + d**0.5) / (2*a), (-b - d**0.5) / (2*a)
	
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
print(solve_quadratic_eqn(a, b, c))