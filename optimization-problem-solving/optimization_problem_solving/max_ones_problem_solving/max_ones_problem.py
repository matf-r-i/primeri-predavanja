import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from target_problem.target_problem import TargetProblem

class MaxOnesProblem(TargetProblem):
    def __init__(self, file_path:str )->None:
        """
        Create new TargetProblemMaxOnes instance
        :param file_path:str -- path of the file with data for the parget problem instance 
        """
        super().__init__("TargetProblemMaxOnes", file_path)

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
