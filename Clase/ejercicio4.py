import sympy as sp
import pprint
x = sp.Symbol("x")
y = sp.Function("y")

a = y(x).diff(x)

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
        print("Su solucion:")
        sp.pprint(solucion4)