from .BaseObject import *
import numpy as np

class Polygon(BaseObject): # Convex one

    def __init__(self,
                 vertices,
                 rot = 0,
                 inv = False):
        BaseObject.__init__(self, vertices[0], rot, 'Polygon', inv)
        self.Vertices = np.array(vertices,dtype='float64')
        if rot != 0:
            self.Rotate(rot)
        self.Coefs = np.zeros([len(vertices),3], dtype='float64')
        self.UpdateCoefs()
        self.Curves = [lambda u, i=i: # With normilized signed distance
            (self.Coefs[i,0] * u[0] + self.Coefs[i,1] * u[1] + \
             self.Coefs[i,2]) * self.sgn
        for i in range(-1,len(vertices)-1)]
    
    def _Outline1d(self,u):
        if self.sgn == 1:
            return np.max([f(u) for f in self.Curves])
        else:
            return np.min([f(u) for f in self.Curves])
        
    def Translate(self, dest = None, delta = None):
        if (dest is None) == (delta is None):
            raise ValueError('Only one of \'delta\' or \'dest\' must be defined')
        elif dest is not None:
            delta = dest - self.Origin
        self.Vertices += delta
        self.Origin = self.Vertices[0]
        self.UpdateCoefs()

    def Rotate(self, teta, pol = None):
        if pol is None:
            teta = teta - self.Rot # Leave only angle increment
            self.Rot += teta
            pol = self.Origin
        rot_matrix = np.array([[np.cos(teta),np.sin(teta)],
                               [-np.sin(teta),np.cos(teta)]])
        self.Vertices = (self.Vertices - pol).dot(rot_matrix) + pol
        self.Origin = self.Vertices[0]
        self.UpdateCoefs()
        
    def UpdateCoefs(self): # Call after any vertices changing!
        for i in range(-1,len(self.Vertices)-1):
            Ai = self.Vertices[i,1] - self.Vertices[i+1,1]
            Bi = self.Vertices[i+1,0] - self.Vertices[i,0]
            Ci = self.Vertices[i,0] * self.Vertices[i+1,1] - \
             self.Vertices[i+1,0] * self.Vertices[i,1]
            norm = np.linalg.norm([Ai,Bi])
            self.Coefs[i,0] = Ai / norm
            self.Coefs[i,1] = Bi / norm
            self.Coefs[i,2] = Ci / norm

    def SetMetrices(self, vertices):
        self.Vertices = vertices
        self.UpdateCoefs()

    def GetMetrices(self):
        return self.Vertices