from .BasicPhiFunction import *
from ..Objects.Polygon import *
from ..Objects.CustomObject import *

class CPPhiFunction(BasicPhiFunction):

    def __init__(self,A,B):
        BasicPhiFunction.__init__(self,A,B,'CP')
        if (A.ObjectName == 'Circle') & (B.ObjectName == 'Polygon'):
            self.C = A
            self.P = B
        elif (B.ObjectName == 'Circle') & (A.ObjectName == 'Polygon'):
            self.C = B
            self.P = A
        else:
            raise TypeError('A and B must be a pair of Circle and Polygon')
        self.Hull = Polygon(self.__BuildHull(self.P))
        self.SuperP = CustomObject(self.P.Origin,
                              objects = [self.Hull,self.P],
                              operator = 'And')
        if self.P.sgn == -1:
            self.P.Inverse()
            self.SuperP.Inverse()

    def Evaluate(self):
        self.Hull.Vertices = self.__BuildHull(self.P) # Get rid of it!!!
        self.Hull.UpdateCoefs()
        self.Value = self.SuperP.Outline(self.C.Origin) - self.C.R
        return self.Value
    
    def __BuildHull(self, P): # Optimize it!!!
        coefs = np.empty(P.Coefs.shape)
        for i in range(-1,len(P.Vertices)-1):
            coefs[i] = P.Coefs[i] + P.Coefs[i+1]
        A = coefs[:,0]; B = coefs[:,1]; C = coefs[:,2]
        vertices = np.empty(P.Vertices.shape)
        for i in range(-1,len(P.Vertices)-1):
            x = (B[i] * C[i+1] - B[i+1] * C[i]) / (A[i] * B[i+1] - A[i+1] * B[i])
            y = (C[i] * A[i+1] - C[i+1] * A[i]) / (A[i] * B[i+1] - A[i+1] * B[i])
            vertices[i] = [x,y]
        return vertices