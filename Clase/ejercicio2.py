import sympy as sp
import pprint
x = sp.Symbol("x")
y = sp.Function("y")

a = y(x).diff(x)

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
        print("Su solucion:")
        sp.pprint(solucion2)
        ics = {y(sp.pi/2): sp.exp}
        cond_in = sp.Eq(solucion2.lhs.subs(x, 0).subs(ics), solucion2.rhs.subs(x, 0))
        print("Despejando la condicion inicial:", cond_in)
        resolucion = sp.solve(cond_in)
        print("Resolviendo con la condicion inicial:")
        sp.pprint(resolucion)
        
sol2 = Ecuacion2(x,y,a)
print(sol2)
sol2.resolver()