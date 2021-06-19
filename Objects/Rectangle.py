from .BaseObject import *
from .Polygon import *
import numpy as np

class Rectangle(Polygon):

    def __init__(self,
                 origin,
                 width,
                 height,
                 rot = 0,
                 inv = False):
        self.Width = width
        self.Height = height
        self.Origin = np.array(origin)
        vertices = np.array([self.Origin,
                             self.Origin + (0,height),
                             self.Origin + (width,height),
                             self.Origin + (width,0)])
        Polygon.__init__(self,vertices,rot,inv)

    def SetMetrices(self, width, height):
        self.Width = width
        self.Height = height
        self.Vertices = np.array([self.Origin,
            self.Origin + (0,height),
            self.Origin + (width,height),
            self.Origin + (width,0)])
        self.Rotate(self.Rot,self.Origin)
        self.UpdateCoefs()

    def GetMetrices(self):
        return np.array([self.Width,self.Height])