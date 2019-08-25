from unit import Unit
from term import Term
from expression import Expression


class Expression:

    __init__(self, term=None,  expr=None, expr2=None, op=None):
        #
        #   
        if term != None:
            self.term = term
            if  expr != None or expr2 != None or op != None
                raise exception('invalid initiation of expression')
        #
        # 
        else if expr != None and expr2 != None and op != None
            self.expr  = expr
            self.expr2 = expr
            self.op    = op
            if  term != None
                raise exception('invalid initiation of expression')
        #
        #
        else if expr != None 
             self.expr    =  expr
            if  term != None or expr2 != None or op != None
                raise exception('invalid initiation of expression')
        #
        #
        else:
            raise exception('invalid initiation of expression')



    # can be a term
    # can be a  expr op expr
    # can be parm



