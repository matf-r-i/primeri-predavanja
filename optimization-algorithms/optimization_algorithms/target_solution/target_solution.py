from pathlib import Path
import sys 
path = Path().joinpath().joinpath('..')
sys.path.append(str(path))

from abc import ABC, abstractmethod

class TargetSolution:
    def __init__(self, name:str)->None:
        """
        Create new TargetSolution instance
        :param name:str -- name of the target solution
        """
        self.__name = name
        self.__fitness = None

    def __copy__(self):
        """
        Internal copy of the current target solution
        :return: TargetSolution -- new TargetSolution instance with the same properties
        """
        return TargetSolution(self.__name)

    def copy(self):
        """
        Copy the current target solution
        :return: TargetSolution -- new TargetSolution instance with the same properties
        """
        return self.__copy__()

    @property
    def name(self)->str:
        """
        Property getter for the name of the target solution
        :return: name of the target solution instance 
        """
        return self.__name

    @property
    def fitness_value(self)->float:
        """
        Property getter for fitness value of the target solution
        :return: fitness of the target solution instance 
        """
        return self.__fitness

    @fitness_value.setter
    def fitness_value(self, value:float)->None:
        """
        Property setter for dimension of the target solution
        """
        if value < 0:
            raise ValueError("Fitness less than 0 is not possible.")
        self.__fitness = value

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the target solution instance
        :return: string representation of the target solution instance
        """
        s = 'name= '+ self.name + '| '
        return s

    @abstractmethod
    def __repr__(self)->str:
        """
        Representation of the target solution instance
        :return: string representation of the solution instance
        """
        s = 'name= '+ self.name + '\n'
        return s

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the target solution instance
        :param spec: str -- Format specification
        :return: formatted target solution instance
        """
        s = 'name= '+ self.name + '| '
        return s
