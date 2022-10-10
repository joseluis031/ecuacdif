import sympy as sp
x = sp.Symbol("x")
y = sp.Function("y")

def ecuacion1():
    
    a = y(x).diff(x)
    ec1 = x**2*y(x)-y(x) / y(x)+1
    a1 =sp.Eq(a, ec1) #expresar ecuacion
    print("La ecuacion 1 es:", a1)
    solucion = sp.dsolve(a-ec1) #resolver ecuacion
    print("Su solucion:",solucion)
    
ecuacion1()


def ecuacion2():
    b = y(x).diff(x)
    ec2 = (y(x)*sp.log(y(x)))/sp.sin(x) #con sympy log"=="ln
    a2 =sp.Eq(b, ec2)
    print("La ecuacion 2 es:", a2)
    solucion2 = sp.dsolve(b-ec2)
    print("Su solucion:",solucion2)
    
ecuacion2()

def ecuacion3():
    c = y(x).diff(x)
    ec3 = (2*((x-2)**2)) + y(x)/x-2
    a3 =sp.Eq(c, ec3)
    print("La ecuacion 3 es:", a3)
    solucion3 = sp.dsolve(c-ec3)
    print("Su solucion:",solucion3)

ecuacion3()