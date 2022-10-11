import sympy as sp
x = sp.Symbol("x")
y = sp.Function("y")

a = y(x).diff(x)


class Ecuacion1:
    def __init__(self,x,y,a):
        self.x = x
        self.y = y
        self.a = a
        self.ec1 = x**2*y(x)-y(x) / y(x)+1
        self.a1 =sp.Eq(a, self.ec1) #expresar ecuacion


    def __str__(self):
        return f"La ecuacion 1 es: {self.a1}"
        
    def resolver(self):
        
        solucion = sp.dsolve(a-self.ec1) #resolver ecuacion
        print("Su solucion:",solucion)
    
sol1 = Ecuacion1
print(sol1)
sol1.resolver()


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

def ecuacion4():
    d = y(x).diff(x)
    ec4 = (3*x**2 + y(x))/2*x
    a4 =sp.Eq(d, ec4)
    print("La ecuacion 4 es:", a4)
    solucion4 = sp.dsolve(d-ec4)
    print("Su solucion:",solucion4)
    
ecuacion4()    
   

 