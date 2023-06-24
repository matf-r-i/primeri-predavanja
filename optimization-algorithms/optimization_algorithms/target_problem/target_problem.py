from pathlib import Path
import sys 
path = Path().joinpath().joinpath('..')
sys.path.append(str(path))

from abc import ABC, abstractmethod

class TargetProblem:
    def __init__(self, name:str, file_path:str )->None:
        """
        Create new TargetProblem instance
        :param name:str -- name of the target problem
        :param file_path:str -- path of the file with data for the parget problem instance 
        """
        self.__name = name
        self.__file_path = file_path

    def __copy__(self):
        """
        Internal copy of the current target problem
        :return: TargetProblem -- new TargetProblem instance with the same properties
        """
        return TargetProblem(self.__name, self.__file_path)

    def copy(self):
        """
        Copy the current target problem
        :return: TargetProblem -- new TargetProblem instance with the same properties
        """
        return self.__copy__()

    @property
    def name(self)->str:
        """
        Property getter for the name of the target problem
        :return: name of the target problem instance 
        """
        return self.__name

    @property
    def file_path(self)->str:
        """
        Property getter for the file path of the target problem
        :return: file path of the target problem instance 
        """
        return self.__file_path

    @property
    def dimension(self)->int:
        """
        Property getter for dimension of the target problem
        :return: dimension of the target problem instance 
        """
        return self.__dimension

    @dimension.setter
    def dimension(self, value:int)->None:
        """
        Property setter for dimension of the target problem
        """
        if value < 0:
            raise ValueError("Dimension less than 0 is not possible.")
        self.__dimension = value

    @abstractmethod
    def load_from_file(data_representation: str)->None:
        """
        Read target problem data from file
        :param data_representation: str -- Data representation within file
        """
        pass

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the target problem instance
        :return: string representation of the target problem instance
        """
        s = '<Problem>' + '\n'
        s += 'name: '+ self.name + '\n'
        s += 'file path: '+ str(self.file_path) 
        return s

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the target problem instance
        :param spec: str -- Format specification
        :return: formatted target problem instance
        """
        s = '<Problem>' + '\n'
        s += 'name: '+ self.name + '\n'
        s += 'file path: '+ str(self.file_path) 
        return s
