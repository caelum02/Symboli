from symboli.operators import Operator, Function
from abc import ABC, abstractmethod
import numpy as np
from symboli.expression import Expression

class ExpFunc(Function):
    def __init__(self, *operands):
        super(ExpFunc, self).__init__(*operands)
    
    def evaluate(self):
        return np.exp(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\exp'

class SinFunc(Function):
    def __init__(self, *operands):
        super(SinFunc, self).__init__(*operands)

    def evaluate(self):
        return np.sin(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\sin'

class CosFunc(Function):
    def __init__(self, *operands):
        super(CosFunc, self).__init__(*operands)
    
    def evaluate(self):
        return np.cos(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\cos'

class TanFunc(Function):
    def __init__(self, *operands):
        super(TanFunc, self).__init__(*operands)
    
    def evaluate(self):
        return np.tan(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\tan'

class CotFunc(Function):
    def __init__(self, *operands):
        super(CotFunc, self).__init__(*operands)
    
    def evaluate(self):
        return np.cot(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\cot'

class SecFunc(Function):
    def __init__(self, *operands):
        super(SecFunc, self).__init__(*operands)
    
    def evaluate(self):
        return np.sec(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\sec'

class CscFunc(Function):
    def __init__(self, *operands):
        super(CscFunc, self).__init__(*operands)
    
    def evaluate(self):
        return np.csc(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\csc'

class LogFunc(Function):
    def __init__(self, *operands):
        super(LogFunc, self).__init__(*operands)
    
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