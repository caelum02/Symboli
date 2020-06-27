from symboli.operators import Operator
from abc import ABC, abstractmethod
import numpy as np
from symboli.expression import Expression

class Function(Operator, ABC):
    def __init__(self, *operands):
        self.operands = operands
    
    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def toTex(self):
        pass

class ExpFunc(Function):
    def __init__(self, *operands):
        super(exp, self).__init__(*operands)
    
    def evaluate(self):
        return np.exp(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\exp'

class SinFunc(Function):
    def __init__(self, *operands):
        super(sin, self).__init__(*operands)

    def evaluate(self):
        return np.sin(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\sin'

class CosFunc(Function):
    def __init__(self, *operands):
        super(cos, self).__init__(*operands)
    
    def evaluate(self):
        return np.cos(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\cos'

class TanFunc(Function):
    def __init__(self, *operands):
        super(tan, self).__init__(*operands)
    
    def evaluate(self):
        return np.tan(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\tan'

class CotFunc(Function):
    def __init__(self, *operands):
        super(cot, self).__init__(*operands)
    
    def evaluate(self):
        return np.cot(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\cot'

class SecFunc(Function):
    def __init__(self, *operands):
        super(sec, self).__init__(*operands)
    
    def evaluate(self):
        return np.sec(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\sec'

class CscFunc(Function):
    def __init__(self, *operands):
        super(csc, self).__init__(*operands)
    
    def evaluate(self):
        return np.csc(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\csc'

class LogFunc(Function):
    def __init__(self, *operands):
        super(log, self).__init__(*operands)
    
    def evaluate(self):
        return np.log(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\log'

def exp(operand):
    return Expression(ExpFunc(operand), operand)

def sin(operand):
    return Expression(SinFunc(operand), operand)

def cos(operand):
    return Expression(CosFunc(operand), operand)

def tan(operand):
    return Expression(TanFunc(operand), operand)

def csc(operand):
    return Expression(CscFunc(operand), operand)

def sec(operand):
    return Expression(SecFunc(operand), operand)

def cot(operand):
    return Expression(CotFunc(operand), operand)