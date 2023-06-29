import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from typing import Dict, TypeVar

from metaheuristic import Metaheuristic

from target_problem.target_problem import TargetProblem

from target_solution.target_solution import TargetSolution

S = TypeVar("S", bound=TargetSolution) 

class VnsOptimizer(Metaheuristic):
    
    def __init__(self, is_minimization:bool, evaluations_max:int=0, seconds_max:int=0, random_seed:int=0, 
        target_problem:TargetProblem=None)->None:
        """
        Create new VnsOptimizer instance
        :param is_minimization:bool -- is minimum is seek for
        :param evaluations_max:int -- maximum number of evaluations for algorithm execution
        :param seconds_max:int -- maximum number of seconds for algorithm execution
        :param random_seed:int -- random seed for metaheuristic execution
        :param target_problem:TargetProblem -- problem to be solved
        """
        super().__init__('vns', is_minimization, evaluations_max, seconds_max, random_seed, target_problem)

    def __copy__(self):
        """
        Internal copy of the current VnsOptimizer
        :return: VnsOptimizer -- new VnsOptimizer instance with the same properties
        """
        return VnsOptimizer(self.__name, self.__is_minimization, self.__evaluations_max, self.__target_problem)

    def copy(self):
        """
        Copy the current VnsOptimizer instance
        :return: VnsOptimizer -- new VnsOptimizer instance with the same properties
        """
        return self.__copy__()

    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the metaheuristic algorithm
        """
        pass

    def init(self)->None:
        """
        Initialization of the metaheuristic algorithm
        """
        pass

    def string_representation(self, delimiter:str)->str:
        """
        String representation of the VnsOptimizer instance
        :param delimiter: str -- Delimiter between fields
        :return: str -- string representation of VnsOptimizer instance
        """        
        s = super().string_representation(delimiter)
        return s

    def __str__(self)->str:
        """
        String representation of the VnsOptimizer instance
        :return: str -- string representation of the VnsOptimizer instance
        """
        s = self.string_representation('|')
        return s;

    def __repr__(self)->str:
        """
        String representation of the VnsOptimizer instance
        :return: str -- string representation of the VnsOptimizer instance
        """
        s = self.string_representation('\n')
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the VnsOptimizer instance
        :param spec: str -- Format specification 
        :return: str -- formatted VnsOptimizer instance
        """
        s = self.string_representation('|')
        return s