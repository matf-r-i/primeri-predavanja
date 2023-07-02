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
        self.__dimension:int = None

    def __copy__(self):
        """
        Internal copy of the MaxOnesProblem problem
        :return: MaxOnesProblem -- new MaxOnesProblem instance with the same properties
        """
        pr = MaxOnesProblem(self.__file_path)
        pr.dimension = self.dimension
        return pr

    def copy(self):
        """
        Copy the MaxOnesProblem problem
        :return: MaxOnesProblem -- new MaxOnesProblem instance with the same properties
        """
        return self.__copy__()

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

    def load_from_file(self, data_representation:str)->None:
        """
        Read target problem data from file
        :param data_representation: str -- data representation within file
        """
        logger.debug("Load parameters: file path={}, data format representation={}".format(self.file_path, 
                data_representation))
        if data_representation=='txt':
                input_file = open(self.file_path, 'r')
                text_line = input_file.readline().strip()
                # skip comments
                while text_line.startswith("//") or text_line.startswith(";"):
                    text_line = input_file.readline()
                self.dimension = int( text_line.split()[0] )

        else:
            raise ValueError('Value for data format \'{} \' is not supported'.format(data_representation))

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
        s = delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start + delimiter
        s+= super().string_representation(delimiter, indentation, indentation_symbol, '', '')
        s+= delimiter
        for i in range(0, indentation):
            s += indentation_symbol 
        s += 'dimension=' + str(self.dimension) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
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


