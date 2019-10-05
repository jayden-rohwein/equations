class Variable:

    def __init__(self,name,unit):
        self.unit = unit
        self.name = name
        self.type = "variable"
        self.value = ""
        self.hasValue = False


    def setValue(self, value):
        self.value = value
        self.hasValue = True
    
    def removeValue(self):
        self.hasValue = False

    def copy(self, name):
        copy = Variable(name, self.unit)
        copy.hasValue = self.hasValue
        copy.value = self.value
        return copy