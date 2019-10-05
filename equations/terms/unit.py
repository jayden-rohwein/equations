#  -- does not have any values
# -- just a list for numorators & denominators
#
#
class Unit:

    def __init__(self, unit=None, num=[], den=[]):
        if unit != None:
            self.numorator   = unit.numorator[:]
            self.denominator = unit.denominator[:]
        else:
            self.numorator   = num
            self.denominator = den


    
    def mul(self,unit):
        product = Unit(self)
        
        for e in unit.numorator:
            if e in product.denominator:
                product.denominator.remove(e)
            else:
                product.numorator.append(e)
        
        for e in unit.denominator:
            if e in product.numorator:
                product.numorator.remove(e)
            else:
                product.denominator.append(e)
        

        return product.simplify(product)
                


    def div(self,unit):
        product = Unit(self)
        
        for e in unit.denominator:
            if e in product.denominator:
                product.denominator.remove(e)
            else:
                product.numorator.append(e)
        

        for e in unit.numorator:
            if e in product.numorator:
                product.numorator.remove(e)
            else:
                product.denominator.append(e)
        

        return product.simplify(product)




    def simplify(self):
        simplified = Unit(self)
        for i in self.numorator:
            for j in self.denominator:
                if i == j:
                    simplified.numorator.remove(i)
                    simplified.denominator.remove(i)
                    
        return simplified
                    



    def toString(self):
        string = ""

        if len(self.numorator) == 0 and len(self.denominator) == 0:
            return  'no units'

        if len(self.numorator) > 0:
            for i in self.numorator:
                string = string + i + " "
            if len(self.denominator) > 0:
                string = string + 'per '
                for i in self.denominator:
                    string = string + i + " "
        else :
            string.append("1 / ")
            for i in self.numorator:
                string = string + i + " "
        return string


