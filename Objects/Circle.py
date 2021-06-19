from .BaseObject import *

class Circle(BaseObject):
    
    def __init__(self,
                 origin,
                 r,
                 inv = False):
        BaseObject.__init__(self, origin, 0, 'Circle', inv)
        self.R = r
        self.Curves = [lambda u: 
            ((self.Origin[0] - u[0]) ** 2 + (self.Origin[1] - u[1]) ** 2 - \
              self.R ** 2) * self.sgn]
        
    def _Outline1d(self,u):
        return self.Curves[0](u)
            
    def Translate(self, dest = None, delta = None):
        if (dest is None) == (delta is None):
            raise ValueError('Only one of \'delta\' or \'dest\' must be defined')
        elif dest is not None:
            delta = dest - self.Origin
        self.Origin += delta

    def Rotate(self, teta, pol = None):
        if pol is None:
            return
        rot_matrix = np.array([[np.cos(teta),np.sin(teta)],
                               [-np.sin(teta),np.cos(teta)]])
        self.Origin = (self.Origin - pol).dot(rot_matrix) + pol

    def SetMetrices(self, r):
        self.R = r

    def GetMetrices(self):
        return self.R