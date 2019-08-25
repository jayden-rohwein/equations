from unit import Unit

class Term:

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self.sigfig = self.getSigfig(value) 

    #----------------------------  make this actually get significant figures
    def getSigfig(self, value):  
        return 2
 
    def mul(self, term):
        new_sigfig =  min(self.sigfig, term.sigfig)
        new_value  =  self.value * term.value  #----- this will eventually have to be a function to incorporate sig fig & floating point
        new_unit   =  self.unit.mul(term.unit)
        return Term(new_value, new_unit)


    def div(self, term):
        new_sigfig =  min(self.sigfig, term.sigfig)
        new_value  =  self.value / term.value  #----- this will eventually have to be a function to incorporate sig fig & floating point
        new_unit   =  self.unit.div(term.unit)
        return Term(new_value, new_unit)

    def toString(self):
        return (str(self.value) + "  " + self.unit.toString())




# speed = Term( 55, Unit(num=['Kilo', 'Meter'],den=['Hour']))
# time  = Term( 2, Unit(num=['Hour']))
# distance = speed.mul(time)
# mystery = speed.div(time)
# print(speed.toString())
# print(time.toString())
# print(distance.toString())
# print(mystery.toString())
