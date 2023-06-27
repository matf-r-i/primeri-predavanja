import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from abc import ABCMeta, abstractmethod
from algorithm.algorithm import Algorithm

class Metaheuristic(Algorithm, metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self, name:str, is_minimization:bool, evaluations_max:int=None)->None:
        """
        Create new Metaheuristic instance
        :name:str -- name of the metaheuristic
        """
        super().__init__(name, is_minimization, evaluations_max)

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

    def string_representation(self, delimiter:str)->str:
        """
        String representation of the Metaheuristic instance
        :param delimiter: str -- Delimiter between fields
        :return: string representation of Metaheuristic instance
        """        
        s = super().string_representation(delimiter)
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the Metaheuristic instance
        :return: string representation of the Metaheuristic instance
        """
        s = self.string_representation('|')
        return s;

    @abstractmethod
    def __repr__(self)->str:
        """
        String representation of the Metaheuristic instance
        :return: string representation of the Metaheuristic instance
        """
        s = self.string_representation('\n')
        return s

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the Metaheuristic instance
        :param spec: str -- Format specification
        :return: formatted Metaheuristic instance
        """
        s = self.string_representation('|')
        return s