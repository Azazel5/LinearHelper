from sympy import *

class LinearSolver:
# A class which uses the sympy functions to solve linear algebra problems useful for me
# ---------------------------------------------------------------------------------------
# Using these functions, I will check the answers to my linear homework/exam answers 

    def __init__(self, matrix):
        self.matrix = matrix
    
    # Returns a tuple, second value is the pivot columns of the matrix
    def reduced_row_echelon_form(self):
        return self.matrix.rref()

    # Non-square matrices don't have inverses 
    def inverse(self):
        return self.matrix**-1
    
    def transpose(self):
        return self.matrix.T

    # Calculates Nul A; dim Nul A = len(nullspace)
    def nullspace(self):
        return self.matrix.nullspace()

    # Calculates Col A; dim Col A = len(columnspace)
    def columnspace(self):
        return self.matrix.columnspace()

    def determinant(self):
        return self.matrix.det()

    # Returns eigenvalues as a list so I can check the value of zero for the invertible matrix theorem
    def eigenvalues(self):
        return list(self.matrix.eigenvals().keys())

    # Matrix not invertible only if it isn't 0
    def isInvertible(self):
        return self.determinant() != 0 or 0 in self.eigenvalues()

    # Returns a tuple in the following format: (eigenvalue:algebraic multiplicity, [eigenvectors]).
    def eigen_info(self):
        return self.matrix.eigenvects()

    def characteristic(self):
        lamda = symbols('λ')
        pol = self.matrix.charpoly(lamda)
        return factor(pol)

    # Returns a tuple (P, D), where M = PDP^-1
    def diagonalize(self):
        return self.matrix.diagonalize()


M = Matrix([
    [1, 5, 0],
    [2, 4, -1],
    [0, -2, 0]
])

matrix = LinearSolver(M)
print(matrix.isInvertible())



