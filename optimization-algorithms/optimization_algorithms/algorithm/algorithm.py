from pathlib import Path
import sys 
path = Path().joinpath().joinpath('..')
sys.path.append(str(path))

from abc import ABCMeta, abstractmethod

class Algorithm(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, name:str, is_minimization:bool, evaluations_max:int=None)->None:
        """
        Create new Algorithm instance
        :param name:str -- name of the algorithm
        :param is_minimization:bool -- is minimum is seek for
        :param evaluations_max:int -- maximum number of evaluations
        """
        self.__name = name
        self.__is_minimization = is_minimization
        self.__evaluations_max = evaluations_max

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current algorithm
        :return: Algorithm -- new Algorithm instance with the same properties
        """
        return Algorithm(self.__name, self.__is_minimization, self.__evaluations_max)

    @abstractmethod
    def copy(self):
        """
        Copy the current algorithm
        :return: Algorithm -- new Algorithm instance with the same properties
        """
        return self.__copy__()

    @property
    def name(self)->str:
        """
        Property getter for the name of the algorithm
        :return: name of the algorithm instance 
        """
        return self.__name

    @property
    def is_minimization(self)->bool:
        """
        Property getter for the name of the algorithm
        :return: if minimization takes place 
        """
        return self.__is_minimization

    @property
    def evaluations_max(self)->int:
        """
        Property getter for the maximum number of evaluations
        :return: maximum number of evaluations 
        """
        return self.__evaluations_max

    def string_representation(self, delimiter:str)->str:
        """
        String representation of the Algorithm instance
        :param delimiter: str -- Delimiter between fields
        :return: string representation of the Algorithm instance
        """        
        s = delimiter + 'name=' + self.name + delimiter
        s += 'is_minimization=' + str(self.is_minimization) + delimiter
        s += 'evaluations_max=' + str(self.evaluations_max) + delimiter
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the algorithm instance
        :return: string representation of the algorithm instance
        """
        return self.string_representation('|')

    @abstractmethod
    def __repr__(self)->str:
        """
        Representation of the algorithm instance
        :return: string representation of the problem instance
        """
        return self.string_representation('\n')

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the algorithm instance
        :param spec: str -- Format specification
        :return: formatted algorithm instance
        """
        return self.string_representation('|')
