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
        target_problem:TargetProblem=None, initial_solution:S=None, k_min:int=1, k_max:int=3, 
                max_local_optima:int=1)->None:
        """
        Create new VnsOptimizer instance
        :param is_minimization:bool -- is minimum is seek for
        :param evaluations_max:int -- maximum number of evaluations for algorithm execution
        :param seconds_max:int -- maximum number of seconds for algorithm execution
        :param random_seed:int -- random seed for metaheuristic execution
        :param target_problem:TargetProblem -- problem to be solved
        :param initial_solution:S -- initial solution of the problem that is optimized by VNS 
        :param k_min:int -- k_min parameter for VNS
        :param k_max:int -- k_max parameter for VNS
        :param max_local_optima:int -- max_local_optima parameter for VNS
        """
        super().__init__('vns', is_minimization, evaluations_max, seconds_max, random_seed, target_problem)
        self.__current_solution = initial_solution
        self.__k_min = k_min
        self.__k_max = k_max
        self.__max_local_optima = max_local_optima
        self.__local_optima:Dict[str, float] = {}

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

    @property
    def current_solution(self)->S:
        """
        Property getter for the current solution used during VNS execution
        :return: instance of the TargetSolution class subtype -- current solution of the problem 
        """
        return self.__current_solution

    @property
    def k_min(self)->int:
        """
        Property getter for the k_min parameter for VNS
        :return: int -- k_min parameter for VNS 
        """
        return self.__k_min

    @property
    def k_max(self)->int:
        """
        Property getter for the k_max parameter for VNS
        :return: int -- k_max parameter for VNS 
        """
        return self.__k_max

    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the VNS algorithm
        """
        pass

    def init(self)->None:
        """
        Initialization of the VNS algorithm
        """
        pass

    def string_representation(self, delimiter:str)->str:
        """
        String representation of the VnsOptimizer instance
        :param delimiter: str -- Delimiter between fields
        :return: str -- string representation of VnsOptimizer instance
        """        
        s = super().string_representation(delimiter)
        s += 'current_solution={' + str(self.current_solution) + '}' + delimiter 
        s += 'k_min=' + str(self.k_min) + delimiter 
        s += 'k_max=' + str(self.k_max) 
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