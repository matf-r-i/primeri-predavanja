import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import random

from abc import ABCMeta, abstractmethod

from algorithm.algorithm import Algorithm

from target_problem.target_problem import TargetProblem

from solution_code_distance_cache_control_statistics import SolutionCodeDistanceCacheControlStatistics

from target_solution.target_solution import TargetSolution


class Metaheuristic(Algorithm, metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self, name:str, is_minimization:bool, evaluations_max:int=0, seconds_max:int=0, random_seed:int=0, target_problem:TargetProblem=None)->None:
        """
        Create new Metaheuristic instance
        :name:str -- name of the metaheuristic
        :param is_minimization:bool -- is minimum is seek for
        :param evaluations_max:int -- maximum number of evaluations for algorithm execution
        :param seconds_max:int -- maximum number of seconds for algorithm execution
        :param random_seed:int -- random seed for metaheuristic execution
        :param target_problem:TargetProblem -- problem to be solved
        """
        super().__init__(name, is_minimization, evaluations_max, seconds_max, target_problem)
        if random_seed is not None and isinstance(random_seed, int) and random_seed != 0:
            self.__random_seed = random_seed
        else:
            self.__random_seed = random.randrange(sys.maxsize)
        self.__iteration = 0
        self.__iteration_best_found = 0
        self.__second_best_found = 0.0
        self.__best_solution = None
        self.__all_solution_codes = {}
        self.__solution_code_distance_cache_cs = SolutionCodeDistanceCacheControlStatistics(is_caching=True)

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current metaheuristic
        :return: Metaheuristic -- new Metaheuristic instance with the same properties
        """
        return Metaheuristic(self.__name, self.__is_minimization, self.__evaluations_max, self.__target_problem)

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

    @abstractmethod
    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the metaheuristic algorithm
        """
        pass

    @abstractmethod
    def init(self)->None:
        """
        Initialization of the metaheuristic algorithm
        """
        pass

    def elapsed_seconds(self)->float:
        """
        Calculate time elapsed during execution of the metaheuristic algorithm 
        :return: float -- elapsed time (in seconds)
        """
        delta = datetime.now() - self.__execution_started
        return delta.total_seconds()

    def main_loop(self)->None:
        """
        Main loop of the metaheuristic algorithm
        """
        while self.evaluation < self.evaluations_max and self.elapsed_seconds() < self.__seconds_max:
                main_loop_iteration(self)

    def optimize(self)->None:
        """
        Executing optimization by the metaheuristic algorithm
        """
        self.__execution_started = datetime.now();
        self.init();
        self.main_loop();
        self.__execution_ended = datetime.now();

    def is_first_solution_better(self, sol1:TargetSolution, sol2:TargetSolution)->bool:
        """
        Checks if first solution is better than the second one
        :param sol1:TargetSolution -- First solution
        :param sol2:TargetSolution -- Second solution
        :return: bool -- true if first solution is better, false if first solution is worse, None if fitnesses of both solutions are equal
        """
        fit1 = sol1.fitness_value;
        fit2 = sol2.fitness_value;
        # with fitness is better than without fitness
        if fit1 is None:
            if fit2 is not None:
                return False
            else:
                return None
        elif fit2 is None:
            return True
        # if better, return true
        if (self.is_minimization and fit1 < fit2) or (not self.is_minimization and fit1 > fit2):
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
        :param solution:TargetSolution -- Source solution
        """
        if self.__best_solution is None:
            self__best_solution = solution.copy()
        else:
            solution.copy_to(self__best_solution)
        self.__second_best_found = (datetime.now() - self.__execution_started).total_seconds()
        self.__iteration_best_found = iteration

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

    def string_representation(self, delimiter:str, indentation:int=0, indentation_start:str ='{', 
        indentation_end:str ='}')->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- Delimiter between fields
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
        s += 'random_seed=' + str(self.random_seed) + delimiter
        s += '__iteration=' + str(self.__iteration) + delimiter
        s += '__iteration_best_found=' + str(self.__iteration_best_found) + delimiter
        s += '__second_best_found=' + str(self.__second_best_found) + delimiter
        if self.__best_solution is not None:
            s += '__best_solution=' + self.__best_solution.string_representation(delimiter=delimiter, 
                    indentation=indentation+1) + delimiter
        else:
            s += '__best_solution=None' + delimiter
        s += '__solution_code_distance_cache_cs=' + self.__solution_code_distance_cache_cs.string_representation(
                delimiter=delimiter, indentation=indentation+1) + delimiter
        if self.execution_ended is not None and self.execution_started is not None:
            s += 'execution time=' + str( (self.execution_ended - self.execution_started).total_seconds() ) + delimiter
        s += 'total local optima found=' + str(len(self.__all_solution_codes)) 
        for i in range(0, indentation):
            s += indentation_end 
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
        :param spec: str -- Format specification
        :return: str -- formatted Metaheuristic instance
        """
        s = self.string_representation('|')
        return s