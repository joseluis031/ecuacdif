from sympy import *

init_printing()
x = symbols("x")
y = Function("y")

3*y(x).diff(x)
