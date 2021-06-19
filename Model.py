from .Objects import *
from .Functions import *
from .Container import *
from .CostFunction import *
import numpy as np

class Model:
    
    def __init__(self, objects, container, cost_func):
        if container is not cost_func.Container:
            raise ValueError('\'container\' must be the same as in \'objective\'')
        if container in objects:
            raise ValueError('\'container\' should not present in \'objects\'')
        self.Objects = objects
        self.Container = container
        self.CostFunction = cost_func
        self.ObjectsState = np.zeros(len(objects) * 3, dtype='float64')
        self.ContainerState = np.zeros(cost_func.InputDim, dtype='float64')
        self.InputDim = self.ContainerState.shape[0] + self.ObjectsState.shape[0]
        self.State = np.zeros(self.InputDim, dtype='float64')
        self.Offsets = []
        for i in range(len(objects)):
            self.Offsets.append(cost_func.InputDim + i * 3)
        self.UpdateState()
        self.PhiFunctions = self.__BuildFunctions(objects,container)
        self.ConstraintsNumber = len(self.PhiFunctions)
        self.FunctionsValues = np.zeros(self.ConstraintsNumber)
        
    def __BuildFunctions(self,objects,container):
        f_list = []
        for i in range(len(objects)):
            f = build_phi_function(objects[i],container.Object)
            f_list.append(f)
            for j in range(i+1,len(objects)):
                f = build_phi_function(objects[i],objects[j])
                f_list.append(f)
        return f_list
            
    def Objective(self,x):
        return self.CostFunction.Evaluate(*x[:self.CostFunction.InputDim])
        
    def Constraints(self, x):
        self.ImplementState(x)
        self.UpdateState()
        return self.EvaluateFunctions()
        
    def ImplementState(self, x):
        self.Container.Modify(*x[:self.CostFunction.InputDim])
        for i in range(len(self.Objects)):
            j = self.Offsets[i]
            self.Objects[i].Locate(self.State[j:j+3])
    
    def UpdateState(self):
        self.State[:self.CostFunction.InputDim] = self.Container.MetricParams
        for i in range(len(self.Objects)):
            j = self.Offsets[i]
            self.State[j] = self.Objects[i].Origin[0]
            self.State[j+1] = self.Objects[i].Origin[1]
            self.State[j+2] = self.Objects[i].Rot
    
    def EvaluateFunctions(self):
        for i in range(self.ConstraintsNumber):
            self.FunctionsValues[i] = self.PhiFunctions[i].Evaluate()
        return self.FunctionsValues