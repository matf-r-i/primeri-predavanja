import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from random import choice
from random import random

from typing import Dict, TypeVar, Generic

from metaheuristic import Metaheuristic

from target_problem.target_problem import TargetProblem

from target_solution.target_solution import TargetSolution

from algorithm.metaheuristic.variable_neighborhood_search.target_solution_vns_support import TargetSolutionVnsSupport

S_co = TypeVar("S_co", covariant=True, bound=TargetSolution) # and bound by TargetSolutionVnsSupport 

class VnsOptimizer(Metaheuristic, Generic[S_co]):
    
    def __init__(self, is_minimization:bool, evaluations_max:int=0, seconds_max:int=0, random_seed:int=0, 
        keep_all_solution_codes:bool=False, target_problem:TargetProblem=None, initial_solution:S_co=None, 
        k_min:int=1, k_max:int=3, max_local_optima:int=3, local_search_type:str='local_search_best_improvement' )->None:
        """
        Create new VnsOptimizer instance
        :param is_minimization:bool -- is minimum is seek for
        :param evaluations_max:int -- maximum number of evaluations for algorithm execution
        :param seconds_max:int -- maximum number of seconds for algorithm execution
        :param random_seed:int -- random seed for metaheuristic execution
        :param keep_all_solution_codes:bool -- if all solution codes will be remembered
        :param target_problem:TargetProblem -- problem to be solved
        :param initial_solution:S -- initial solution of the problem that is optimized by VNS 
        :param k_min:int -- k_min parameter for VNS
        :param k_max:int -- k_max parameter for VNS
        :param max_local_optima:int -- max_local_optima parameter for VNS
        """
        super().__init__('vns', is_minimization, evaluations_max, seconds_max, random_seed, keep_all_solution_codes,
                target_problem)
        self.__current_solution:S_co = initial_solution
        self.__k_min = k_min
        self.__k_max = k_max
        self.__max_local_optima = max_local_optima
        self.__local_search_type = local_search_type        
        self.__local_optima:Dict[str, float] = {}
        self.__shaking_counts:Dict[int,int] = {}

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
    def current_solution(self)->S_co:
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

    def init(self)->None:
        """
        Initialization of the VNS algorithm
        """
        self.__k_current = self.k_min
        self.current_solution.evaluate();
        self.copy_to_best_solution(self.current_solution);

    def __select_shaking_points__(self)->list[str]:
        """
        Selecting shaking point for the VNS algorithm
        :return: list[str] -- list with solution codes that represents start of the shaking 
        """
        return [self.current_solution.solution_code]

    def __add_local_optima__(self, current_solution:TargetSolution)->bool:
        """
        Add solution to the local optima structure 
        :param current_solution:TargetSolution -- solution to be added to local optima structure
        :return: bool -- if adding is successful e.g. current_solution is new element in the structure
        """       
        if current_solution.solution_code in self.__local_optima:
            return False
        if len(self.__local_optima) >= self.__max_local_optima:
            # removing random, just taking care not to remove the best ones
            while True:
                code = random.choice(self.__local_optima.keys())
                if code != self.best_solution.solution_code:
                    del self.__local_optima[code]
                    break
        self.__local_optima[current_solution.solution_code]=current_solution.fitness_value
        return True

    def __shaking_ls__(self)->bool:
        """
        Shaking phase of the VNS algorithm
        :return: bool -- if result obtain by shaking is better than initial
        """
        shaking_points = self.__select_shaking_points__()
        if not self.current_solution.randomize(self.__k_current, shaking_points):
            return False
        if self.__k_current in self.__shaking_counts:
            self.__shaking_counts[self.__k_current] += 1
        else:
            self.__shaking_counts[self.__k_current] = 1
        self.iteration += 1
        self.evaluation += 1
        self.current_solution.evaluate()
        if self.__local_search_type == 'local_search_best_improvement':
            self.current_solution = self.local_search_best_improvement(self.current_solution)
        else:
            raise ValueError( 'Value \'{} \' for VNS local_search_type is not supported'.format(
                    self.__local_search_type))
        logger.debug(self.current_solution)
        if self.keep_all_solution_codes:
            self.all_solution_codes.add(self.current_solution)
        new_is_better = self.is_first_solution_better(self.current_solution, self.best_solution);
        if new_is_better is None:
            logger.debug("Same solution quality, generating random true with probability 0.5");
            return random.random() < 0.5
        return new_is_better

    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the VNS algorithm
        """
        while self.shaking():
            self.copy_to_best_solution(self.current_solution)
            self.__k_current = self.k_min
        if self.__k_current < self.k_max:
            self.__k_current += 1
        else:
            self.__k_current = self.k_min

    def string_representation(self, delimiter:str, indentation:int=0, indentation_start:str ='{', 
        indentation_end:str ='}')->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- delimiter between fields
        :param indentation:int -- level of indentation
        :param indentation_start -- indentation start string 
        :param indentation_end -- indentation end string 
        :return: str -- string representation of target solution instance
        """             
        s = ''
        for i in range(0, indentation):
            s += indentation_start  
        s = super().string_representation(delimiter)
        s += delimiter
        s += 'current_solution=' + self.current_solution.string_representation(delimiter=delimiter, 
                indentation=indentation+1) + delimiter 
        s += 'k_min=' + str(self.k_min) + delimiter 
        s += 'k_max=' + str(self.k_max) 
        s += '__max_local_optima=' + str(self.__max_local_optima) 
        s += '__local_search_type=' + str(self.__local_search_type) 
        for i in range(0, indentation):
            s += indentation_end 
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
        :param spec: str -- format specification 
        :return: str -- formatted VnsOptimizer instance
        """
        s = self.string_representation('|')
        return s