import numpy as np

class PhiFunction:
    
    def __init__(self,A,B,func_type = ''):
        for obj in [A,B]:
            if obj.ObjectType not in ['BaseObject','CustomObject']:
                raise TypeError(f'Wrong object type \'{type(obj)}\'')
        self.A = A
        self.B = B
        self.FunctionType = func_type
        self.Value = None

    def Evaluate(self):
        pass