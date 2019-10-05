from unit import Unit
from term import Term
from variable import variable
from expression import expression




class equation:
    __init__(self, expr_left, expr_right){
        self.expr_left = expr_left
        self.expr_right = expr_right
        self.type = "equation"
    }


