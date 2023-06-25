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

    def __str__(self)->str:
        """
        String representation of the max ones problem instance
        :return: string representation of the max ones problem instance
        """
        return super().__str__()

    def __repr__(self)->str:
        """
        String representation of the max ones problem instance
        :return: string representation of the max ones problem instance
        """
        return super().__repr__()

    def __format__(self, spec:str)->str:
        """
        Formatted the target problem instance
        :param spec: str -- Format specification
        :return: formatted target problem instance
        """
        return super().__format__(spec)

    def load_from_file(self, data_representation: str)->None:
        """
        Read target problem data from file
        :param data_representation: str -- Data representation within file
        """
        logger.debug("Load parameters: file path ={}, data format representation ={}".format(self.file_path, data_representation))
