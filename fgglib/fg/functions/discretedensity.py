from fgglib.base.semiring import Real
from fgglib.fg.factorfunction import FactorFunction

import numpy as np

class DiscreteDensity(FactorFunction):
    # for now we limit to random variable with a contingous subset {0, 1, ... X} of N as codomain
    
    def __init__(self, raw_pmf):
        self.pmf = np.asarray(raw_pmf, dtype=np.float64)
        super().__init__(Real, len(self.pmf.shape))
            
    def compute(self, *args) -> Real:
        return self.pmf[arg]
    
    '''
    def __mul__(self, other):
        return DiscreteDensity(self.pmf * other.pmf)
            
    def summary(self, arg_index) -> FactorFunction:
        return DiscreteDensity(np.sum(self.pmf, (arg_index)))
        
    def normalization_constant(self) -> Real:
        return np.abs(np.sum(self.pmf))
        
    def normalize(self):
        return DiscreteDensity(self.pmf / self.normalization_constant())
    '''