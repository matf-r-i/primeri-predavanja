import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from algorithm.algorithm import Algorithm

class Metaheuristic(Algorithm):
    def __init__(self, name:str )->None:
        """
        Create new TargetProblemMaxOnes instance
        :name:str -- name of the metaheuristic
        """
        super().__init__(name)

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