import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from copy import deepcopy
from random import choice
from random import random
from typing import TypeVar, Generic
from typing import Generic

from utils.logger import logger
from target_problem.target_problem import TargetProblem
from target_solution.target_solution import TargetSolution
from algorithm.metaheuristic.metaheuristic import Metaheuristic
from algorithm.metaheuristic.variable_neighborhood_search.vns_support_for_target_solution import VnsSupportForTargetSolution

S_co = TypeVar("S_co", covariant=True, bound=TargetSolution) # and bound by VnsSupportForTargetSolution 

class VnsOptimizer(Metaheuristic, Generic[S_co]):
    
    def __init__(self, evaluations_max:int, seconds_max:int, random_seed:int, keep_all_solution_codes:bool, 
            target_problem:TargetProblem, initial_solution:S_co, k_min:int, k_max:int, max_local_optima:int, 
            local_search_type:str)->None:
        """
        Create new VnsOptimizer instance
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
        super().__init__('vns', evaluations_max, seconds_max, random_seed, keep_all_solution_codes, target_problem)
        self.__current_solution:S_co = initial_solution
        self.__k_min:int = k_min
        self.__k_max:int = k_max
        self.__max_local_optima:int = max_local_optima
        self.__local_search_type:str = local_search_type        
        self.__k_current:int = None
        self.__local_optima:Dict[str, float] = {}
        self.__shaking_counts:Dict[int,int] = {}

    def __copy__(self):
        """
        Internal copy of the current VnsOptimizer
        :return: VnsOptimizer -- new VnsOptimizer instance with the same properties
        """
        vns_opt = deepcopy(self)
        return vns_opt

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

    @current_solution.setter
    def current_solution(self, value:S_co)->None:
        """
        Property setter for for the current solution used during VNS execution
        :param value:S_co -- the current solution
        """
        self.__current_solution = value

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
        self.current_solution.evaluate(self.target_problem);
        self.copy_to_best_solution(self.current_solution);

    def __select_shaking_points__(self)->list[str]:
        """
        Selecting shaking point for the VNS algorithm
        :return: list[str] -- list with solution codes that represents start of the shaking 
        """
        return [self.current_solution.solution_code()]

    def __add_local_optima__(self, current_solution:TargetSolution)->bool:
        """
        Add solution to the local optima structure 
        :param current_solution:TargetSolution -- solution to be added to local optima structure
        :return: bool -- if adding is successful e.g. current_solution is new element in the structure
        """       
        if current_solution.solution_code() in self.__local_optima:
            return False
        if len(self.__local_optima) >= self.__max_local_optima:
            # removing random, just taking care not to remove the best ones
            while True:
                code = random.choice(self.__local_optima.keys())
                if code != self.best_solution.solution_code():
                    del self.__local_optima[code]
                    break
        self.__local_optima[current_solution.solution_code()]=current_solution.fitness_value
        return True

    def __shaking_ls__(self)->bool:
        """
        Shaking phase of the VNS algorithm
        :return: bool -- if result obtain by shaking is better than initial
        """
        #logger.debug('__shaking_ls__ - start')
        #logger.debug('Current: {}'.format(self.current_solution))
        #logger.debug('Best: {}'.format(self.current_solution))
        shaking_points:list[str] = self.__select_shaking_points__()
        if not self.current_solution.vns_randomize(self.target_problem, self.__k_current, shaking_points):
            return False
        if self.__k_current in self.__shaking_counts:
            self.__shaking_counts[self.__k_current] += 1
        else:
            self.__shaking_counts[self.__k_current] = 1
        self.iteration += 1
        self.evaluation += 1
        self.current_solution.evaluate(self.target_problem)
        if self.__local_search_type == 'local_search_best_improvement':
            self.current_solution = self.local_search_best_improvement(self.current_solution)
        else:
            raise ValueError( 'Value \'{} \' for VNS local_search_type is not supported'.format(
                    self.__local_search_type))
        if self.keep_all_solution_codes:
            self.all_solution_codes.add(self.current_solution)
        new_is_better = self.is_first_solution_better(self.current_solution, self.best_solution)
        if new_is_better is None:
            if self.current_solution.solution_code() == self.best_solution.solution_code():
                return False
            else:
                logger.debug("Same solution quality, generating random true with probability 0.5");
                return random() < 0.5
        #logger.debug('__shaking_ls__ - end')
        #logger.debug('Current: {}'.format(self.current_solution))
        #logger.debug('Best: {}'.format(self.current_solution))
        return new_is_better

    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the VNS algorithm
        """
        while self.__shaking_ls__():
            self.copy_to_best_solution(self.current_solution)
            self.__k_current = self.k_min
        if self.__k_current < self.k_max:
            self.__k_current += 1
        else:
            self.__k_current = self.k_min

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='',group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- delimiter between fields
        :param indentation:int -- level of indentation
        :param indentation_symbol:str -- indentation symbol
        :param group_start -- group start string 
        :param group_end -- group end string 
        :return: str -- string representation of target solution instance
        """             
        s = delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s = super().string_representation(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += 'current_solution=' + self.current_solution.string_representation(delimiter, indentation + 1, 
                indentation_symbol, group_start, group_end) + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'k_min=' + str(self.k_min) + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'k_max=' + str(self.k_max) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__max_local_optima=' + str(self.__max_local_optima) + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__local_search_type=' + str(self.__local_search_type) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
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
        return self.string_representation('\n',0,'   ','{', '}')
