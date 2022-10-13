import sympy as sp
import pprint
x = sp.Symbol("x")
y = sp.Function("y")

a = y(x).diff(x)


class Ecuacion1:
    def __init__(self,x,y,a):
        self.x = x
        self.y = y
        self.a = a
        self.ec1 = (x**2*y(x)-y(x)) / y(x)+1
        self.a1 =sp.Eq(a, self.ec1) #expresar ecuacion


    def __str__(self):
        return f"La ecuacion 1 es: {self.a1}"
        
    def resolver(self):
        
        solucion = sp.dsolve(a-self.ec1) #resolver ecuacion
        print("Su solucion:")
        sp.pprint(solucion)
        ics = {y(3): -1}
        cond_in = sp.Eq(solucion.lhs.subs(x, 3).subs(ics), solucion.rhs.subs(x, 3))
        print("Despejando la condicion inicial:", cond_in)
        resolucion = sp.solve(cond_in)
        print("Resolviendo con la condicion inicial:")
        sp.pprint(resolucion)
