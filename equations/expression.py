from terms.unit import Unit
from terms.op import Op
from terms.variable import Variable

class Expression:

    def __init__(self, expr):
        self.variables = {}
        self.type = "expression"
        self.expr = expr

        for e in expr:
            if( hasattr(e, 'type')   and  e.type == "variable"):
                self.variables[e.name] =  e


    def allVarHaveValue(self):
        for key in self.variables:
            if( self.variables[key].hasValue == False):
                return False
        return True


    def toString(self):
        s = "variables:\n"
        for key in self.variables:
            s = s + key + " " +  str(self.variables[key].value) + "\n"

        s = s + "expression:\n"
        for e in self.expr:
                s = s + e.name + " "

        return s


    
    #
    #           TODO
    #
    #
    #def nextAlgebrah(self):
    #def calculate():










A = Variable("A" , "meters")
A.setValue(5)
B = A.copy("B")
B.setValue(3)
C = Variable("C", "meters")

add = Op("+")
mul = Op("*")

list = []
list.append(A)
list.append(add)
list.append(B)
list.append(mul)
list.append(C)

exp = Expression(list)
print exp.toString()
print exp.allVarHaveValue()








