import path
import sys 

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent)

from copy import deepcopy
from abc import ABCMeta, abstractmethod

class TargetProblem(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, name:str, is_minimization:bool, file_path:str)->None:
        """
        Create new TargetProblem instance
        :param name:str -- name of the target problem
        :param is_minimization:bool --should minimum or maximum be determined
        :param file_path:str -- path of the file with data for the target problem instance 
        """
        self.__name:str = name
        self.__is_minimization = is_minimization
        self.__file_path:str = file_path
        self.__dimension:int = None

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current target problem
        :return: TargetProblem -- new TargetProblem instance with the same properties
        """
        pr = deepcopy(self)
        return pr

    @abstractmethod
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
        :return: str -- name of the target problem instance 
        """
        return self.__name

    @property
    def is_minimization(self)->bool:
        """
        Property getter for the name of the algorithm
        :return: bool -- if minimization takes place 
        """
        return self.__is_minimization

    @property
    def file_path(self)->str:
        """
        Property getter for the file path of the target problem
        :return: str -- file path of the target problem instance 
        """
        return self.__file_path

    @property
    def dimension(self)->int:
        """
        Property getter for dimension of the target problem
        :return: int -- dimension of the target problem instance 
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
        Read target problem data from file and set intrinsic data
        :param data_representation: str -- data representation within file
        """
        raise NotImplementedError

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the target problem instance
        :param delimiter: str -- delimiter between fields
        :param indentation:int -- level of indentation
        :param indentation_symbol:str -- indentation symbol
        :param group_start -- group start string 
        :param group_end -- group end string 
        :return: str -- string representation of target problem instance
        """          
        s =  delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'name=' + self.name + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'is_minimization=' + str(self.is_minimization) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'file path=' + str(self.file_path) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol 
        s += 'dimension=' + str(self.dimension) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the target problem instance
        :return: str -- string representation of the target problem instance
        """
        return self.string_representation('|')

    @abstractmethod
    def __repr__(self)->str:
        """
        Representation of the target problem instance
        :return: str -- string representation of the problem instance
        """
        return self.string_representation('\n')

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the target problem instance
        :param spec: str -- format specification
        :return: str -- formatted target problem instance
        """
        return self.string_representation('|')

