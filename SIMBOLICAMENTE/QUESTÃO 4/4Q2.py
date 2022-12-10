from sympy import*
init_printing(pretty_print=True)

x = Symbol('x')

print(float(integrate(asin(sqrt(x))/(sqrt(x*(1 - x))),(x,0,1) )))