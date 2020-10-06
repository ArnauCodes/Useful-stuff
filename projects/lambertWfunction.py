from scipy.special import lambertw
from math import sqrt, e

# Using lambert W function with example equation
print("Lambert W function examples\ngiven x^2*e^x = 2")
input()
print("Square root both sides to get, x * e^x/2 = +-sqrt(2)") 
input("Everything good until now, however, in this step, the lambert W functionwould be used if x/2 was multipying e or if the exponent of e was only x")
input()
print("The lambert W function is used as W(x*e^x) = x, where x >= -1/e")
input()
print("But we still do not have the same terms, so in order to make the exponent equal to x, we gotta divide two to both sides")
input()
print("Then we will have x/2*e^x/2 = +- sqrt(2)/2 and we can apply the lambert W function correctley")
input()
print("So we get W(x/2*e^x/2) = W(+-sqrt(2)/2)")
input()
print("After applied we get that x/2 = W(+-sqrt(2)), but -sqrt(2) is less than -1 / e, so discard the -sqrt(2) answer")
input()
print("To finish, if we only multpily both sides by two so x/2 cancels and we get 2*W(sqrt(2))")
input("Here we will plot in the decimal value for x, as x = 2*W(sqrt(2)):")
x = 2*lambertw(sqrt(2) / 2)
sq_x = x**2
e_to_x = pow(e, x)
print(f"The decimal value for x = {x} wihtout the complex part. So having x^2 will give us {sq_x} that multpilies by e^x.\ne^x is {e_to_x}.And finally we have to multplliy it by {sq_x}. The final answer is 1.9999...\n which is basically aproximation of 2")
