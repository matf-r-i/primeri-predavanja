import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from random import random
from copy import deepcopy
from datetime import datetime
from abc import ABCMeta, abstractmethod

from utils.logger import logger
from algorithm.algorithm import Algorithm
from solution_code_distance_cache_control_statistics import SolutionCodeDistanceCacheControlStatistics
from target_problem.target_problem import TargetProblem
from target_solution.target_solution import TargetSolution

class Metaheuristic(Algorithm, metaclass=ABCMeta):
    
    """
    Cache that is used during calculation of the solution code distances
    """
    solution_code_distance_cache_cs:SolutionCodeDistanceCacheControlStatistics = SolutionCodeDistanceCacheControlStatistics()

    @abstractmethod
    def __init__(self, name:str, evaluations_max:int, seconds_max:int, random_seed:int, 
            keep_all_solution_codes:bool, target_problem:TargetProblem)->None:
        """
        Create new Metaheuristic instance
        :name:str -- name of the metaheuristic
        :param evaluations_max:int -- maximum number of evaluations for algorithm execution
        :param seconds_max:int -- maximum number of seconds for algorithm execution
        :param random_seed:int -- random seed for metaheuristic execution
        :param keep_all_solution_codes:bool -- if all solution codes will be remembered        
        :param target_problem:TargetProblem -- problem to be solved
        """
        super().__init__(name, evaluations_max, seconds_max, target_problem)
        if random_seed is not None and isinstance(random_seed, int) and random_seed != 0:
            self.__random_seed:int = random_seed
        else:
            self.__random_seed:int = random.randrange(sys.maxsize)
        self.__iteration:int = 0
        self.__iteration_best_found:int = 0
        self.__second_when_best_obtained:float = 0.0
        self.__best_solution:TargetSolution = None
        self.__keep_all_solution_codes:bool = keep_all_solution_codes
        self.__all_solution_codes:set[str] = set()

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current metaheuristic
        :return: Metaheuristic -- new Metaheuristic instance with the same properties
        """
        met = deepcopy(self)
        return met

    @abstractmethod
    def copy(self):
        """
        Copy the current metaheuristic
        :return: Metaheuristic -- new Metaheuristic instance with the same properties
        """
        return self.__copy__()

    @property
    def random_seed(self)->int:
        """
        Property getter for the random seed used during metaheuristic execution
        :return: int -- random seed 
        """
        return self.__random_seed

    @property
    def iteration(self)->int:
        """
        Property getter for the iteration of metaheuristic execution
        :return: int -- iteration
        """
        return self.__iteration

    @iteration.setter
    def iteration(self, value:int)->None:
        """
        Property setter the iteration of metaheuristic execution
        :param value:datetime -- iteration
        """
        self.__iteration = value

    @property
    def best_solution(self)->TargetSolution:
        """
        Property getter for the best solution obtained during metaheuristic execution
        :return: TargetSolution -- best solution so far 
        """
        return self.__best_solution

    @property
    def keep_all_solution_codes(self)->bool:
        """
        Property getter for decision should be kept all solution codes
        :return: bool -- decision should be kept all solution codes
        """
        return self.__keep_all_solution_codes

    @property
    def all_solution_codes(self)->set[str]:
        """
        Property getter for the all solution codes
        :return: set[str] -- all solution codes
        """
        return self.__all_solution_codes

    @all_solution_codes.setter
    def all_solution_codes(self, value:set[str])->None:
        """
        Property setter the all solution codes
        :param value:set[str] -- all solution codes
        """
        self.__all_solution_codes = value

    @abstractmethod
    def init(self)->None:
        """
        Initialization of the metaheuristic algorithm
        """
        raise NotImplementedError

    @abstractmethod
    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the metaheuristic algorithm
        """
        raise NotImplementedError

    def elapsed_seconds(self)->float:
        """
        Calculate time elapsed during execution of the metaheuristic algorithm 
        :return: float -- elapsed time (in seconds)
        """
        delta = datetime.now() - self.execution_started
        return delta.total_seconds()

    def local_search_best_improvement(self, solution:TargetSolution)->TargetSolution:
        """
        Executes best improvement variant of the local search procedure 
        :param solution:TargetSolution -- solution which is initial point for local search
        :return: TargetSolution -- result of the local search procedure 
        """
        while True:
            if not solution.best_1_change(self.target_problem):
                break
        return solution

    def main_loop(self)->None:
        """
        Main loop of the metaheuristic algorithm
        """
        while (self.evaluations_max == 0 or self.evaluation < self.evaluations_max) and (self.seconds_max == 
                0 or self.elapsed_seconds() < self.seconds_max):
            self.main_loop_iteration()
            logger.debug('Iteration:{}, Evaluations:{}, Bit code:{}'.format(self.iteration, self.evaluation,
                str(self.best_solution.representation)))

    def optimize(self)->None:
        """
        Executing optimization by the metaheuristic algorithm
        """
        self.execution_started = datetime.now();
        self.init();
        self.main_loop();
        self.execution_ended = datetime.now();

    def is_first_solution_better(self, sol1:TargetSolution, sol2:TargetSolution)->bool:
        """
        Checks if first solution is better than the second one
        :param sol1:TargetSolution -- first solution
        :param sol2:TargetSolution -- second solution
        :return: bool -- true if first solution is better, false if first solution is worse, None if fitnesses of both 
                solutions are equal
        """
        if self.target_problem is None:
            raise ValueError('Target problem have to be defined within metaheuristic.')
        if self.target_problem.is_minimization is None:
            raise ValueError('Information if minimization or maximization is set within metaheuristic target problem'
                    'have to be defined.')
        is_minimization:bool = self.target_problem.is_minimization
        if sol1 is None:
            fit1:float = None
        else:
            fit1:float = sol1.calculate_objective_fitness_feasibility(self.target_problem).fitness_value;
        if sol2 is None:
            fit2:float = None
        else:
            fit2:float = sol2.calculate_objective_fitness_feasibility(self.target_problem).fitness_value;
        # with fitness is better than without fitness
        if fit1 is None:
            if fit2 is not None:
                return False
            else:
                return None
        elif fit2 is None:
            return True
        # if better, return true
        if (is_minimization and fit1 < fit2) or (not is_minimization and fit1 > fit2):
            return True
        # if same fitness, return None
        if fit1 == fit2:
            return None
        # otherwise, return false
        return False

    def copy_to_best_solution(self, solution:TargetSolution)->None:
        """
        Copies function argument to become the best solution within metaheuristic instance and update info about time 
        and iteration when the best solution is updated 
        :param solution:TargetSolution -- solution that is source for coping operation
        """
        self.__best_solution = solution.copy()
        self.__second_when_best_obtained = (datetime.now() - self.execution_started).total_seconds()
        self.__iteration_best_found = self.iteration

    def calculate_solution_code_distance_try_consult_cache(self, code_x:str, code_y:str)->float:
        """
        Calculate distance between two solution codes with optional cache consultation
        :param code_x:str -- first solution code 
        :param code_y:str -- second solution code 
        :return: float -- distance between solution codes 
        """
        if code_x == code_y:
            return 0;
        scdc = self.__solution_code_distance_cache_cs 
        scdc.requests_count += 1
        if scdc.is_caching: 
            if code_x in scdc.cache and code_y in scdc.cache[code_x]:
                scdc.hit_count += 1
                return scdc.cache[code_x][code_y]
            dist = TargetSolution.solution_code_distance(code_x, code_y)
            if code_x not in scdc.cache:
                scdc.cache[code_x] = {};
            scdc.cache[code_x][code_y] = dist;
            return dist;
        else:
            dist = TargetSolution.solution_code_distance(code_x, code_y)
            return dist

    def wtrite_to_output():
        pass

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
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
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'random_seed=' + str(self.random_seed) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__iteration=' + str(self.__iteration) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__iteration_best_found=' + str(self.__iteration_best_found) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__second_when_best_obtained=' + str(self.__second_when_best_obtained) + delimiter
        if self.__best_solution is not None:
            s += '__best_solution=' + self.__best_solution.string_representation(delimiter, indentation + 1,
                    indentation_symbol, group_start, group_end) + delimiter
        else:
            for i in range(0, indentation):
                s += indentation_symbol  
            s += '__best_solution=None' + delimiter
        s += 'solution_code_distance_cache_cs(static)=' + self.solution_code_distance_cache_cs.string_representation(
                delimiter, indentation + 1, indentation_symbol, '{', '}') + delimiter
        if self.execution_ended is not None and self.execution_started is not None:
            for i in range(0, indentation):
                s += indentation_symbol  
            s += 'execution time=' + str( (self.execution_ended - self.execution_started).total_seconds() ) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'total local optima found=' + str(len(self.__all_solution_codes)) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s


    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the Metaheuristic instance
        :return: str -- string representation of the Metaheuristic instance
        """
        s = self.string_representation('|')
        return s

    @abstractmethod
    def __repr__(self)->str:
        """
        String representation of the Metaheuristic instance
        :return: str -- string representation of the Metaheuristic instance
        """
        s = self.string_representation('\n')
        s += '__all_solution_codes=' + str(self.__all_solution_codes) 
        return s

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the Metaheuristic instance
        :param spec: str -- format specification
        :return: str -- formatted Metaheuristic instance
        """
        return self.string_representation('|')
