from .PhiObject import *
import numpy as np

class CustomObject(PhiObject):
        
    def __init__(self,
                 origin,
                 rot = 0,
                 inv = False,
                 objects = [],
                 operator = ''):
        PhiObject.__init__(self, origin, rot, 'CustomObject',inv)
        if (len(objects) == 0) & (len(operator) == 0):
            pass
        elif (len(objects) != 0) & (len(operator) != 0):
            self.AddObjects(objects,operator)
        else:
            raise ValueError('Both of \'objects\' and \'operator\' \
must be defined or none of them')
        self.ObjectCounter = len(self.Objects)

    def Inverse(self):
        PhiObject.Inverse(self)
        self.Operator = 'Or' if self.Operator == 'And' else 'And'
        for obj in self.Objects:
            obj.Inverse()
    
    def _Outline1d(self,u):
        if self.Operator == 'Or':
            return np.min([obj.Outline(u) for obj in self.Objects])
        elif self.Operator == 'And':
            return np.max([obj.Outline(u) for obj in self.Objects])
        
    def Translate(self, dest = None, delta = None):
        if (dest is None) == (delta is None):
            raise ValueError('Only one of \'delta\' or \'dest\' must be defined')
        elif dest is not None:
            delta = dest - self.Origin
        self.Origin += delta
        for i in range(self.ObjectCounter):
            self.Objects[i].Translate(delta = delta)

    def Rotate(self, teta, pol = None):
        if pol is None:
            if teta == self.Rot:
                return
            teta = teta - self.Rot # Leave only angle increment
            self.Rot += teta
            pol = self.Origin
        for obj in self.Objects:
            obj.Rotate(teta,pol)

    def AddObjects(self,objects,operator):
        if operator in ['And','Or']:
            self.Operator = operator
        else:
            raise ValueError(f'Unknown operator \'{operator}\'')
        if len(objects) != 0:
            for obj in objects:
                if obj.ObjectType not in ['BaseObject','CustomObject']:
                    raise TypeError(f'Wrong object type \'{type(obj)}\'')
            self.Objects = objects
    
    def Join(self,objects):
        self.AddObjects(objects, 'Or')
                
    def Intersect(self,objects):
        self.AddObjects(objects, 'And')