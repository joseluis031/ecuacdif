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
    
sol1 = Ecuacion1(x,y,a)
print(sol1)
sol1.resolver()


class Ecuacion2:
    def __init__(self,x,y,a):
        self.x = x
        self.y = y
        self.a = a
        self.ec2 = (y(x)*sp.log(y(x)))/sp.sin(x) #con sympy log"=="ln
        self.a2 =sp.Eq(a, self.ec2)
    
    def __str__(self):
        return f"La ecuacion 2 es:{self.a2}"
    
    def resolver(self):
        
        solucion2 = sp.dsolve(a-self.ec2)
        print("Su solucion:",solucion2)
    
sol2 = Ecuacion2(x,y,a)
print(sol2)
sol2.resolver()



class Ecuacion3():
    def __init__(self,x,y,a):
        self.x = x
        self.y = y
        self.a = a        
        self.ec3 = (2*((x-2)**2)) + y(x)/x-2
        self.a3 =sp.Eq(a, self.ec3)
        
    def __str__(self):
        return f"La ecuacion 3 es: {self.a3}"
    
    def resolver(self):
        
        solucion3 = sp.dsolve(a-self.ec3)
        print("Su solucion:",solucion3)

sol3 = Ecuacion3(x,y,a)
print(sol3)
sol3.resolver()



class Ecuacion4:
    def __init__(self,x,y,a):
        self.x = x
        self.y = y
        self.a = a       
        self.ec4 = (3*x**2 + y(x))/2*x
        self.a4 =sp.Eq(a, self.ec4)
        
    def __str__(self):
        return f"La ecuacion 4 es: {self.a4}"

    def resolver(self):
        
        solucion4 = sp.dsolve(a-self.ec4)
        print("Su solucion:",solucion4)
    
sol4 = Ecuacion4(x,y,a)
print(sol4)
sol4.resolver()   

 