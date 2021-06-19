from .BasicPhiFunction import *

class CCPhiFunction(BasicPhiFunction):
    
    def __init__(self,A,B):
        if (A.ObjectName != 'Circle') | (B.ObjectName != 'Circle'):
            raise TypeError('A and B must be a pair of Circles')
        BasicPhiFunction.__init__(self,A,B,'CC')
    
    def Evaluate(self):
        self.Value = ((self.A.Origin - self.B.Origin) ** 2).sum() \
        - (self.A.R + self.B.R) ** 2
        return self.Value