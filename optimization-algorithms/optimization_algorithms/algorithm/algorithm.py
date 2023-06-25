from pathlib import Path
import sys 
path = Path().joinpath().joinpath('..')
sys.path.append(str(path))

from abc import ABC, abstractmethod

class Algorithm(ABC):

    @abstractmethod
    def __init__(self, name:str )->None:
        """
        Create new Algorithm instance
        :param name:str -- name of the algorithm
        """
        self.__name = name

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current algorithm
        :return: Algorithm -- new Algorithm instance with the same properties
        """
        return Algorithm(self.__name)

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

    def string_representation( self, delimiter:str)->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- Delimiter between fields
        :return: tring representation of target solution instance
        """        
        s = 'name= '+ self.name + delimiter
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the algorithm instance
        :return: string representation of the algorithm instance
        """
        return self.string_representation('| ')

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
        return self.string_representation('| ')
