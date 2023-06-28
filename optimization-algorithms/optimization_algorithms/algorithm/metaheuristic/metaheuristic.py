import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import random

from abc import ABCMeta, abstractmethod

from algorithm.algorithm import Algorithm

from target_problem.target_problem import TargetProblem


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
        self.__all_solution_codes = {}

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

    def string_representation(self, delimiter:str)->str:
        """
        String representation of the Metaheuristic instance
        :param delimiter: str -- Delimiter between fields
        :return: str -- string representation of Metaheuristic instance
        """        
        s = super().string_representation(delimiter)
        s += 'random_seed=' + str(self.random_seed) + delimiter
        s += '__iteration=' + str(self.__iteration) + delimiter
        s += '__iteration_best_found=' + str(self.__iteration_best_found) + delimiter
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the Metaheuristic instance
        :return: str -- string representation of the Metaheuristic instance
        """
        s = self.string_representation('|')
        return s;

    @abstractmethod
    def __repr__(self)->str:
        """
        String representation of the Metaheuristic instance
        :return: str -- string representation of the Metaheuristic instance
        """
        s = self.string_representation('\n')
        s += '__all_solution_codes=' + str(self.__all_solution_codes) + delimiter
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