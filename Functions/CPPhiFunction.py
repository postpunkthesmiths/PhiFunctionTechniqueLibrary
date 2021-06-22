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
        self.chi = np.zeros(self.P.Vertices.shape[0])
        self.omg = np.zeros(self.P.Vertices.shape[0])
        self.psi = np.zeros(self.P.Vertices.shape[0])
        self.Evaluate()

    def Evaluate(self):
        for i in range(self.P.Vertices.shape[0]):
            self.chi[i] = self.P.Curves[i](self.C.Origin) - self.C.R
            self.omg[i] = self.C.Outline(self.P.Vertices[i])
            self.psi[i] = (self.P.Coefs[i-1,1] - self.P.Coefs[i,1]) * (self.C.Origin[0] - self.P.Vertices[i,0]) - \
                          (self.P.Coefs[i-1,0] - self.P.Coefs[i,0]) * (self.C.Origin[1] - self.P.Vertices[i,1]) + \
                          self.C.R * (self.P.Coefs[i-1,0] * self.P.Coefs[i,1] - self.P.Coefs[i,0] * self.P.Coefs[i-1,1])
        self.Value = np.max([
            self.chi,
            np.min([self.omg,self.psi],axis=0)
        ])
        return self.Value