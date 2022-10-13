import sympy as sp
import pprint
x = sp.Symbol("x")
y = sp.Function("y")

a = y(x).diff(x)

class Ecuacion3():
    def __init__(self,x,y,a):
        self.x = x
        self.y = y
        self.a = a        
        self.ec3 = (2*((x-2)**2)) + (y(x)/(x-2))
        self.a3 =sp.Eq(a, self.ec3)
        
    def __str__(self):
        return f"La ecuacion 3 es: {self.a3}"
    
    def resolver(self):
        
        solucion3 = sp.dsolve(a-self.ec3)
        print("Su solucion:")
        sp.pprint(solucion3)
