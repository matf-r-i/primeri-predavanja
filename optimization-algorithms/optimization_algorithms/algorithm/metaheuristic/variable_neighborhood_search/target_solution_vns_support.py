import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from abc import ABCMeta, abstractmethod

class TargetSolutionVnsSupport(metaclass=ABCMeta):
    
    @abstractmethod
    def randomize(k:int, solution_codes:list[str])->bool:
        """
        Randomizes solution codes 
        :param k:int -- parameter for VNS
        :param solution_codes:list[str] -- solution codes that should be randomized
        :return: bool -- if randomization is successful 
        """        
        raise NotImplementedError
