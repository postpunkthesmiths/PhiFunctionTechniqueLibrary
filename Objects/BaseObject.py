from .PhiObject import *

class BaseObject(PhiObject):
    
    def __init__(self, 
                 origin, 
                 rot = 0,
                 obj_name = '',
                 inv = False):
        PhiObject.__init__(self, origin, rot, 'BaseObject', inv)
        self.ObjectName = obj_name
        self.Curves = None

    def SetMetrices(self, r):
        pass

    def GetMetrices(self):
        pass