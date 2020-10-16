# Programme to solve quadratic equations by Completing the square
# The input must only contain a, b, c where a, b, c are real numbers. It is also supposed that the equation's form is of: ax^2 + bx + c = 0
from math import sqrt

a_term = float(0)
b_term = float(1)
c_term = float(0)

def invalid_input():
	return "Invalid Input"


def case_no_b(a, b, c):
	right = c * (-1)
	right /= a_term
	try:
		s = sqrt(right)
	except ValueError as ve:
		return f"No real answers ({ve})"
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
	if a_term != 0 and c_term != 0:
		print(solve(a_term, b_term, c_term))
	elif b_term == 0 and a_term != 0 and c_term != 0:
		print(case_no_b(a_term, b_term, c_term))
	else:
		print(invalid_input())
