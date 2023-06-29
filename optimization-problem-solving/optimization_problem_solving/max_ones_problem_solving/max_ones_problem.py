import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from utils.logger import logger

from target_problem.target_problem import TargetProblem

class MaxOnesProblem(TargetProblem):
    
    def __init__(self, file_path:str )->None:
        """
        Create new MaxOnesProblem instance
        :param file_path:str -- path of the file with data for the parget problem instance 
        """
        super().__init__("MaxOnesProblem", file_path)

    def __copy__(self):
        """
        Internal copy of the MaxOnesProblem problem
        :return: MaxOnesProblem -- new MaxOnesProblem instance with the same properties
        """
        return MaxOnesProblem(self.__file_path)

    def copy(self):
        """
        Copy the MaxOnesProblem problem
        :return: MaxOnesProblem -- new MaxOnesProblem instance with the same properties
        """
        return self.__copy__()

    def load_from_file(self, data_representation: str)->None:
        """
        Read target problem data from file
        :param data_representation: str -- data representation within file
        """
        logger.debug("Load parameters: file path={}, data format representation={}".format(self.file_path, data_representation))

    def string_representation(self, delimiter:str, indentation:int=0, indentation_start:str ='{', 
        indentation_end:str ='}')->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- delimiter between fields
        :param indentation:int -- level of indentation
        :param indentation_start -- indentation start string 
        :param indentation_end -- indentation end string 
        :return: str -- string representation of target solution instance
        """          
        s = ''
        for i in range(0, indentation):
            s += indentation_start 
        s+= super().string_representation(delimiter)
        for i in range(0, indentation):
            s += indentation_end 
        return s

    def __str__(self)->str:
        """
        String representation of the target problem instance
        :return: str -- string representation of the target problem instance
        """
        return self.string_representation('|')

    def __repr__(self)->str:
        """
        Representation of the target problem instance
        :return: str -- string representation of the problem instance
        """
        return self.string_representation('\n')

    def __format__(self, spec:str)->str:
        """
        Formatted the target problem instance
        :param spec: str -- format specification
        :return: str -- formatted target problem instance
        """
        return self.string_representation('|')

