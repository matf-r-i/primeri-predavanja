import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from abc import ABCMeta, abstractmethod

from target_problem.target_problem import TargetProblem

class TargetSolutionVnsSupport(metaclass=ABCMeta):
    
    @abstractmethod
    def vns_randomize(k:int, problem:TargetProblem, solution_codes:list[str])->bool:
        """
        Random VNS shaking of k parts such that new solution code does not differ more than k from all solution codes 
        inside shakingPoints
        :param problem:TargetProblem -- problem that is solved
        :param k:int -- parameter for VNS
        :param solution_codes:list[str] -- solution codes that should be randomized
        :return: bool -- if randomization is successful 
        """        
        raise NotImplemented

