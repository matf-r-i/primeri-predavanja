from pathlib import Path
import sys 
path = Path().joinpath().joinpath('..')
sys.path.append(str(path))

from abc import ABC, abstractmethod

class Algorithm:
    def __init__(self, name:str )->None:
        """
        Create new Algorithm instance
        :param name:str -- name of the algorithm
        """
        self.__name = name

    def __copy__(self):
        """
        Internal copy of the current algorithm
        :return: Algorithm -- new Algorithm instance with the same properties
        """
        return Algorithm(self.__name)

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

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the algorithm instance
        :return: string representation of the algorithm instance
        """
        s = 'name= '+ self.name + '| '
        return s

    @abstractmethod
    def __repr__(self)->str:
        """
        Representation of the algorithm instance
        :return: string representation of the problem instance
        """
        s = 'name= '+ self.name + '| '
        return s

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the algorithm instance
        :param spec: str -- Format specification
        :return: formatted algorithm instance
        """
        s = 'name= '+ self.name + '| '
        return s
