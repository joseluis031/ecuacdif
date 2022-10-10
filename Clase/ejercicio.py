import sympy as sp
x = sp.Symbol("x")
y = sp.Function("y")

def ecuacion1():
    
    a = y(x).diff(x)
    ec1 = x**2*y(x)-y(x) / y(x)+1
    a1 =sp.Eq(a, ec1) #expresar ecuacion
    print("La ecuacion es:", a1)
    solucion = sp.dsolve(a-ec1) #resolver ecuacion
    print(solucion)
    
ecuacion1()


def ecuacion2():
    b = y(x).diff(x)
    ec2 = (y(x)*sp.log(y(x)))/sp.sin(x) #con sympy log"=="ln
    a2 =sp.Eq(b, ec2)
    print("La ecuacion es:", a2)
    solucion2 = sp.dsolve(b-ec2)
    print(solucion2)
    
ecuacion2()