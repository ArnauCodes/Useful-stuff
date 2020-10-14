# Updates are coming
# Programme to solve quadratic equations by Completing the square
# The input must only contain a, b, c where a, b, c are real numbers. It is also supposed that the equation's form is of: ax^2 + bx + c = 0
# -1 is also returned for non-real answers not involving the complex world
from math import sqrt

a_term = float(2)
b_term = float(0)
c_term = float(-3)


def case_no_b(a, b, c):
	right = c * (-1)
	right /= a_term
	try:
		s = sqrt(right)
	except ValueError as ve:
		return (f"No real answers ({ve})")
	else:
		x1 = float(s)
		x2 = float(s * (-1))
	return f"First answer = {x1}\nSecond answer = {x2}"


def solve(a, b, c):
	if a != 0:
		a = 1.0
		b = float(b / (a_term))
		c = float(c / (a_term))
	rside = c * (-1) 
	c = (b / 2)**2 
	r_right = rside + c
	b = b / 2 
	try:
		rtd = sqrt(r_right)
	except ValueError as ve:
		return f"No real answers ({ve})"
	else:
		x1 = float((b * (-1)) + rtd)
		x2 = float((b * (-1)) - rtd)
	return f"First answer = {x1}\nSecond answer = {x2}"


if __name__ == '__main__':
	if b_term == 0:
		print(case_no_b(a_term, b_term, c_term))
	else:
		print(solve(a_term, b_term, c_term))
