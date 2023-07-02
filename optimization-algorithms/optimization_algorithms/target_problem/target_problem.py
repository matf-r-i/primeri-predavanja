from pathlib import Path
import sys 
path = Path().joinpath().joinpath('..')
sys.path.append(str(path))

from abc import ABCMeta, abstractmethod

class TargetProblem(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, name:str, file_path:str)->None:
        """
        Create new TargetProblem instance
        :param name:str -- name of the target problem
        :param file_path:str -- path of the file with data for the target problem instance 
        """
        self.__name:str = name
        self.__file_path:str = file_path

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current target problem
        :return: TargetProblem -- new TargetProblem instance with the same properties
        """
        return TargetProblem(self.__name, self.__file_path)

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
    def file_path(self)->str:
        """
        Property getter for the file path of the target problem
        :return: str -- file path of the target problem instance 
        """
        return self.__file_path

    @abstractmethod
    def load_from_file(data_representation: str)->None:
        """
        Read target problem data from file
        :param data_representation: str -- data representation within file
        """
        raise NotImplementedError

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- delimiter between fields
        :param indentation:int -- level of indentation
        :param indentation_symbol:str -- indentation symbol
        :param group_start -- group start string 
        :param group_end -- group end string 
        :return: str -- string representation of target solution instance
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
        s += 'file path=' + str(self.file_path) + delimiter
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

