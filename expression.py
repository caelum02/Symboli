import operators as op
from symbol import Symbol

class Expression(Symbol):
    def __init__(self, operator, *expr):
        self.operator = operator
        self.expr = list(expr)

        for i, operand in enumerate(self.expr):
            if not isinstance(operand, Symbol):
                self.expr[i] = Constant(str(operand), operand)

    def toTex(self):
        expr_0 = self.expr[0].toTex()
        expr_1 = self.expr[1].toTex()
        oper = self.operator.toTex()

        if isinstance(self.operator, op.BinaryOperator):
            if isinstance(self.operator, (op.SumOp, op.SubOp)):
                return expr_0 + oper + expr_1

            if isinstance(self.operator, (op.MulOp, op.PowOp)):
                if isinstance(self.expr[0].operator, (op.SumOp, op.SubOp)):
                    expr_0 = '\\left(' + expr_0 + '\\right)'
                
                if isinstance(self.expr[1].operator, (op.SumOp, op.SubOp)):
                    expr_1 = '\\left(' + expr_1 + '\\right)'

                return expr_0 + oper + expr_1

            if type(self.operator) == op.DivOp:
                return f'\\frac{{{expr_0}}}{{{expr_1}}}'
        
    def __add__(self, expr):
        return Expression(op.SumOp(self, expr), self, expr)

    def __sub__(self, expr):
        return Expression(op.SubOp(self, expr), self, expr)

    def __mul__(self, expr):
        return Expression(op.MulOp(self, expr), self, expr)

    def __truediv__(self, expr):
        return Expression(op.DivOp(self, expr), self, expr)
    
    def __pow__(self, expr):
        return Expression(op.PowOp(self, expr), self, expr)

    def __radd__(self, expr):
        return Expression(op.SumOp(expr, self), expr, self)

    def evaluate(self):
        return self.operator.evaluate()

class Variable(Expression):
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

        # for convenience
        self.operator = None

    def toTex(self):
        return self.name
    
    def evaluate(self):
        return self.value 

class Constant(Variable):
    def __init__(self, name, value=None):
        self.name = name
        self._value = value

        self.operator = None

    def evaluate(self):
        return self._value


class Matrix(Expression):
    def __init__(self, mat):
        self.mat = mat
        self.shape = self._shape_track()

    def _shape_track(self):
        shape = []
        M = self.mat

        while not isinstance(M, Expression):
            shape.append(len(M))
            M = M[0]

        return tuple(shape)

    def __add__(self, other):
        if isinstance(self.other, Matrix):
            pass
    
if __name__=='__main__':
    r = Variable('r')
    G = Variable('G')
    m = Variable('m')
    M = Variable('M')

    F = G*M*m/r**2

    # rendering
    import matplotlib.pyplot as plt

    ax = plt.axes()
    ax.set_xticks([])
    ax.set_yticks([])
    plt.text(0.5, 0.5, f'$F={F.toTex()}$')

    plt.show()