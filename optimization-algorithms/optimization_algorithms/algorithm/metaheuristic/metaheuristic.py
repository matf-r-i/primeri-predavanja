import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from abc import ABCMeta, abstractmethod

from algorithm.algorithm import Algorithm

from target_problem.target_problem import TargetProblem


class Metaheuristic(Algorithm, metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self, name:str, is_minimization:bool, evaluations_max:int=None, target_problem:TargetProblem=None)->None:
        """
        Create new Metaheuristic instance
        :name:str -- name of the metaheuristic
        :param is_minimization:bool -- is minimum is seek for
        :param evaluations_max:int -- maximum number of evaluations for algorithm execution
        :param seconds_max:int -- maximum number of seconds for algorithm execution
        :param target_problem:TargetProblem -- problem to be solved
        """
        super().__init__(name, is_minimization, evaluations_max, target_problem)

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

    def string_representation(self, delimiter:str)->str:
        """
        String representation of the Metaheuristic instance
        :param delimiter: str -- Delimiter between fields
        :return: str -- string representation of Metaheuristic instance
        """        
        s = super().string_representation(delimiter)
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