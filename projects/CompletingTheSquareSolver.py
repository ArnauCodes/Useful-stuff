# Solve quadratic equations by Completing the square
# The input must only contain a, b, c where a, b, c are real numbers. It is also supposed that the equation's form is of: ax^2 + bx + c = 0
# -1 is also returned for non-real answers not involving the complex world
from math import sqrt

a_term = float(1)
b_term = float(-4)
c_term = float(5)

def solve(a, b, c):
	if a > 0:
		a = 1.0
		b = float(b / a_term)
		c = float(c / a_term)
	rside = c * (-1)
	c = (b / 2)**2
	r_right = rside + c
	b = b / 2
	try:
		rtd = sqrt(r_right)
	except ValueError as ve:
		print(f"No real answers ({ve})")
		return -1
		
	else:
		x1 = int((b * (-1)) + rtd)
		x2 = int((b * (-1)) - rtd)

	return f"First answer = {x1}\nSecond answer = {x2}"
print(solve(a_term, b_term, c_term))
