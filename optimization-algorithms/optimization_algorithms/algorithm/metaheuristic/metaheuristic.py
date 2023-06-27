import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from abc import ABCMeta, abstractmethod
from algorithm.algorithm import Algorithm

class Metaheuristic(Algorithm, metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self, name:str, is_minimization:bool, evaluations_max:int )->None:
        """
        Create new Metaheuristic instance
        :name:str -- name of the metaheuristic
        """
        super().__init__(name, is_minimization)
        __evaluations_max = evaluations_max

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current metaheuristic
        :return: Metaheuristic -- new Metaheuristic instance with the same properties
        """
        return Metaheuristic(self.__name, self.__is_minimization, self.__evaluations_max)

    @abstractmethod
    def copy(self):
        """
        Copy the current metaheuristic
        :return: Metaheuristic -- new Metaheuristic instance with the same properties
        """
        return self.__copy__()

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the Metaheuristic instance
        :return: string representation of the Metaheuristic instance
        """
        s = super().__str__()
        return s;

    @abstractmethod
    def __repr__(self)->str:
        """
        String representation of the Metaheuristic instance
        :return: string representation of the Metaheuristic instance
        """
        s = super().__repr__()
        return s

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the Metaheuristic instance
        :param spec: str -- Format specification
        :return: formatted Metaheuristic instance
        """
        s = super().__format__(spec)
        return s