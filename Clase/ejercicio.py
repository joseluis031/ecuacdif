import sympy
x = sympy.Symbol("x")
y = sympy.Function("y")


a = y(x).diff(x)
ec1 = x**2*y(x)-y(x) / y(x)+1
a1 =sympy.Eq(a, ec1) #expresar ecuacion
print("La ecuacion es:", a1)
solucion = sympy.dsolve(a-ec1) #resolver ecuacion
print(solucion)
