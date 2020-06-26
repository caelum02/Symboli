from symboli.operator import Operator
from abc import ABC, abstractmethod
import numpy as np

class Function(Operator, ABC):
    def __init__(self, *operands):
        self.operands = operands
    
    @abstractmathod
    def evaluate(self):
        pass

    @abstractmethod
    def toTex(self):
        pass

class exp(Function):
    def __init__(self. *operands):
        super(exp, self).__init__(*operands)
    
    def evaluate(self):
        return np.exp(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\exp'

class sin(Function):
    def __init__(self, *operands):
        super(sin, self).__init__(*operands)

    def evaluate(self):
        return np.sin(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\sin'

class cos(Function):
    def __init__(self, *operands):
        super(cos, self).__init__(*operands)
    
    def evaluate(self):
        return np.cos(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\cos'

class tan(Function):
    def __init__(self, *operands):
        super(tan, self).__init__(*operands)
    
    def evaluate(self):
        return np.tan(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\tan'

class cot(Function):
    def __init__(self, *operands):
        super(cot, self).__init__(*operands)
    
    def evaluate(self):
        return np.cot(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\cot'

class sec(Function):
    def __init__(self, *operands):
        super(sec, self).__init__(*operands)
    
    def evaluate(self):
        return np.sec(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\sec'

class csc(Function):
    def __init__(self, *operands):
        super(csc, self).__init__(*operands)
    
    def evaluate(self):
        return np.csc(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\csc'

class log(Function):
    def __init__(self, *operands):
        super(log, self).__init__(*operands)
    
    def evaluate(self):
        return np.log(self.operand[0].evaluate())
    
    def toTex(self):
        return '\\log'

