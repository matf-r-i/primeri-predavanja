import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from target_solution.target_solution import TargetSolution

class MaxOnesSolution(TargetSolution):
    
    def __init__(self)->None:
        """
        Create new MaxOnesSolution instance
        """
        super().__init__("MaxOnesSolution")

    def __copy__(self):
        """
        Internal copy of the MaxOnesSolution problem
        :return: MaxOnesSolution -- new MaxOnesSolution instance with the same properties
        """
        return MaxOnesSolution()

    def copy(self):
        """
        Copy the MaxOnesProblem problem
        :return: MaxOnesProblem -- new MaxOnesProblem instance with the same properties
        """
        return self.__copy__()
        
    def copy_to(self, destination)->None:
        """
        Copy the MaxOnesProblem to the already existing destination MaxOnesProblem
        :param destination:MaxOnesProblem -- destination target problem
        """
        return self.copy_to(destination)
        

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
