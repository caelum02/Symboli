import symboli.operators as op
from symboli.symbol import Symbol
import copy

class Expression(Symbol):
    def __init__(self, operator, *expr):
        self.operator = operator
        self.expr = list(expr)

        for i, operand in enumerate(self.expr):
            if not isinstance(operand, Symbol):
                self.expr[i] = Constant(str(operand), operand)

    def toTex(self):
        expr_0 = self.expr[0].toTex()
        if expr_0[0] == '\\':
            expr_0 += ' '

        oper = self.operator.toTex()

        if isinstance(self.operator, op.BinaryOperator):
            expr_1 = self.expr[1].toTex()

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
            
        elif isinstance(self.operator, op.Function):
            return f'{oper}\\left({expr_0}\\right)'
        
        elif isintance(self.operator, op.UnaryOperator):
            if isinstance(self.expr[0].operator, (op.SumOp, op.SubOp)):
                return oper+f'\\left({expr_0}\\right)'

    def __add__(self, expr):
        if type(expr) == Matrix:
            return expr.__radd__(self)

        return Expression(op.SumOp(self, expr), self, expr)

    def __sub__(self, expr):
        if type(expr) == Matrix:
            return expr.__rsub__(self)

        return Expression(op.SubOp(self, expr), self, expr)

    def __mul__(self, expr):
        if type(expr) == Matrix:
            return expr.__rmul__(self)

        return Expression(op.MulOp(self, expr), self, expr)

    def __truediv__(self, expr):
        if type(expr) == Matrix:
            return expr.__rtruediv__(self)

        return Expression(op.DivOp(self, expr), self, expr)
    
    def __pow__(self, expr):
        return Expression(op.PowOp(self, expr), self, expr)

    def __radd__(self, expr):
        return Expression(op.SumOp(expr, self), expr, self)

    def __rsub__(self, expr):
        return Expression(op.SubOp(expr, self), expr, self)
    
    def __rmul__(self, expr):
        return Expression(op.MulOp(expr, self), expr, self)

    def __rtruediv__(self, expr):
        return Expression(op.DivOp(expr, self), expr, self)

    def __rpow__(self, expr):
        return Expression(op.PowOp(expr, self), expr, self)

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other
    
    def __imul__(self, other):
        return self * other
    
    def __itruediv__(self, other):
        return self / other
    
    def __ipow__(self, other):
        return self ** other

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
        self.value = value

        self.operator = None

    def evaluate(self):
        return self.value

    def __add__(self, other):
        if type(other)==Constant:
            return Constant(str(self.value+other.value), self.value+other.value)

        else:
            super(Constant, self).__add__(other)

    def __sub__(self, other):
        if type(other)==Constant:
            return Constant(str(self.value-other.value), self.value-other.value)
    
        else:
            super(Constant, self).__sub__(other)

    def __mul__(self, other):
        if type(other)==Constant:
            return Constant(str(self.value*other.value), self.value*other.value)
        
        else:
            super(Constant, self).__mul__(other)

    def __truediv__(self, other):
        if type(other)==Constant:
            return Constant(str(self.value/other.value), self.value/other.value)
    
        else:
            super(Constant, self).__truediv__(other)

    def __pow__(self, other):
        if type(other)==Constant:
            return Constant(str(self.value**other.value), self.value**other.value)

        else:
            super(Constant, self).__pow__(other)

    def __neg__(self):
        return Constant(str(-self.value), -self.value)

class Matrix(Expression):
    def __init__(self, mat):
        self.mat = mat
        self.shape = self._shape_track()

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if not isinstance(self.mat[i][j], Symbol):
                    self.mat[i][j] = Constant(str(self.mat[i][j]), self.mat[i][j])

    def _shape_track(self):
        shape = []
        M = self.mat

        while type(M) == list:
            shape.append(len(M))
            M = M[0]

        return tuple(shape)

    def toTex(self):
        texstr = '\\begin{pmatrix}'

        for i in range(self.shape[0]):
            if i != 0:
                texstr += ' \\\\'
            for j in range(self.shape[1]):
                if j!=0:
                    texstr += ' &'
                texstr += f' {self.mat[i][j].toTex()}'

        texstr += ' \\end{pmatrix}'

        return texstr
    
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError

            Mat = copy.deepcopy(self)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    Mat.mat[i][j] += other.mat[i][j]
            
            return Mat
        
        mat = copy.deepcopy(self.mat)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                mat[i][j] += other
        
        return Matrix(mat)

    def __radd__(self, other):
        mat = copy.deepcopy(self.mat)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                mat[i][j] = other + mat[i][j]
        
        return Matrix(mat)
 
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError

            Mat = copy.deepcopy(self)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    Mat.mat[i][j] *= other.mat[i][j]

            return Mat 
        
        mat = copy.deepcopy(self.mat)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                mat[i][j] *= other
        
        return Matrix(mat)
 
    def __rmul__(self, other):
        mat = copy.deepcopy(self.mat)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                mat[i][j] = other * mat[i][j]
        
        return Matrix(mat)

    def __truediv__(self, other):
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError

            Mat = copy.deepcopy(self)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    Mat.mat[i][j] /= other.mat[i][j]
            return Mat 
        
        mat = copy.deepcopy(self.mat)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                mat[i][j] /= other
        
        return Matrix(mat)

    def __rtruediv__(self, other):
        mat = copy.deepcopy(self.mat)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                mat[i][j] = other / mat[i][j]
        
        return Matrix(mat)
     
    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError

            Mat = copy.deepcopy(self)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    Mat.mat[i][j] -= other.mat[i][j]
            return Mat 
        
        mat = copy.deepcopy(self.mat)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                mat[i][j] -= other
        
        return Matrix(mat)
 
    def __rsub__(self, other):
        mat = copy.deepcopy(self.mat)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                mat[i][j] = other - mat[i][j]
        
        return Matrix(mat)

    def __matmul__(self, other):
        if not (type(other)==Matrix):
            raise TypeError

        if not self.shape[1]==other.shape[0]:
            raise ValueError

        mat = [[0]*other.shape[1] for _ in range(self.shape[0])]
        for i in range(self.shape[0]):
            for k in range(other.shape[1]):
                mat[i][k] = self.mat[i][0] * other.mat[0][k]
                for j in range(1, self.shape[1]):
                    mat[i][k] += self.mat[i][j]*other.mat[j][k]
        
        return Matrix(mat)
    
    def evaluate(self):
        evalmat = copy.deepcopy(self.mat)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                evalmat[i][j] = evalmat[i][j].evaluate()
        
        return evalmat

def matfromshape(name, shape):
    if not (type(shape)==tuple):
        raise ValueError
    
    mat = [[Variable(f'{name}_{{{i+1}{j+1}}}') for j in range(shape[1])] for i in range(shape[0])]
    
    return Matrix(mat)


if __name__=='__main__':
    A = matfromshape('a', (3, 4))
    B = matfromshape('b', (4, 2))
    C = matfromshape('c', (2, 5))
    D = matfromshape('d', (3, 4))

    a = Variable('\\alpha')

    print(A+a)
    print(A-a)
    print(A/a)
    print(A*a)