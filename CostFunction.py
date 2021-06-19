class CostFunction:
    
    def __init__(self, container, func):
        self.Container = container
        self.__eval = func
        self.Value = self.Evaluate(*self.Container.MetricParams)
        self.InputDim = len(self.Container.MetricParams)
        
    def Evaluate(self,*args):
        self.Value = self.__eval(*args)
        self.Container.Modify(*args)
        return self.Value