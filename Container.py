import numpy as np

class Container: # Make sure it is inverted finit object!
    
    def __init__(self, obj, modifier, init_state):
        self.Object = obj
        self.ContainerType = obj.ObjectName
        self.MetricParams = np.array(init_state, dtype='float64')
        self.__modifier = modifier
    
    def Modify(self, *args):
        self.__modifier(*args)
        self.MetricParams[:] = args