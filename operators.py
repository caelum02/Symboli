from abc import ABC
from symbol import Symbol
from expression import Constant
import numpy as np

class Operator(Symbol, ABC):
    def _operand_type_check(self):
        if len(self.operands) != self.operand_num:
            raise ValueError

        for i, operand in enumerate(self.operands):
            if not isinstance(operand, Symbol):
                self.operands[i] = Constant(str(operand), operand)
    
class BinaryOperator(Operator):
    def __init__(self, *operands):
        self.operand_num = 2
        self.operands = list(operands)
       
class UnaryOperator(Operator):
    def __init__(self, *operands):
        self.operand_num = 1
        self.operands = list(operands)

class SumOp(BinaryOperator):
    def __init__(self, *operands):
        super(SumOp, self).__init__(*operands)

        self.type = '+'

        self._operand_type_check()

    def evaluate(self):
        return self.operands[0].evaluate() + self.operands[1].evaluate()

    def toTex(self):
        return '+'

class SubOp(BinaryOperator):
    def __init__(self, *operands):
        super(SubOp, self).__init__(*operands)
        self.type = '-'
        self._operand_type_check()

    def evaluate(self):
        return self.operands[0].evaluate() - self.operands[1].evaluate()
    
    def toTex(self):
        return '-'

class MulOp(BinaryOperator):
    def __init__(self, *operands):
        super(MulOp, self).__init__(*operands)
        self.type = '*'
        self._operand_type_check()

    def evaluate(self):
        return self.operands[0].evaluate() * self.operands[1].evaluate()

    def toTex(self):
        return ''

class DivOp(BinaryOperator):
    def __init__(self, *operands):
        super(DivOp, self).__init__(*operands)
        self.type = '/'
        self._operand_type_check()

    def evaluate(self):
        return self.operands[0].evaluate() / self.operands[1].evaluate()
    
    def toTex(self):
        return ''

class PowOp(BinaryOperator):
    def __init__(self, *operands):
        super(PowOp, self).__init__(*operands)
        self.type = '**'
        self._operand_type_check()
    
    def evaluate(self):
        return self.operand[0].evaluate() ** self.operand[1].evaluate()
    
    def toTex(self):
        return '^'

class NegOp(UnaryOperator):
    def __init__(self, *operands):
        super(NegOp, self).__init__(*operands)
        self.type = '-'
        self._operand_type_check()
    
    def evaluate(self):
        return - self.operand[0].evaluate()
    
    def toTex(self):
        return '-'
    
class DiffOp(UnaryOperator):
    '''
        TODO: Implement Differentiation
    '''
    pass

class PartialOp(UnaryOperator):
    '''
        TODO: Implement Partial Differentiation
    '''
    pass

