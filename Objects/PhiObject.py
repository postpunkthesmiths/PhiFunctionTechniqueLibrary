import numpy as np

class PhiObject:
    
    def __init__(self, 
                 origin, 
                 rot = 0,
                 obj_type = '',
                 inv = False):
        self.Origin = np.array(origin,dtype='float64')
        self.Rot = rot
        self.ObjectType = obj_type
        self.sgn = 1
        if inv == True:
            self.Inverse()

    def Inverse(self):
        self.sgn *= -1
        
    def _Outline1d(self,u):
        pass
        
    def Outline(self,u):
        if len(np.shape(u)) == 1:
            return self._Outline1d(u)
        elif len(np.shape(u)) == 2:
            return np.apply_along_axis(self._Outline1d,1,u)
        
    def Locate(self, u): # u - 3d vector
        self.Translate((u[0],u[1]))
        self.Rotate(u[2])
        
    def Translate(self, dest = None, delta = None):
        pass
    
    def Rotate(self, teta, pol = None):
        pass

    def SetMetrices(self):
        pass