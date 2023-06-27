import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from metaheuristic import Metaheuristic

class VnsOptimizer(Metaheuristic):
    
    def __init__(self, is_minimization:bool, evaluations_max:int )->None:
        """
        Create new VnsOptimizer instance
        """
        super().__init__('vns', is_minimization, evaluations_max)

    def __copy__(self):
        """
        Internal copy of the current metaheuristic
        :return: Metaheuristic -- new Metaheuristic instance with the same properties
        """
        return VnsOptimizer(self.__name, self.__is_minimization, self.__evaluations_max)

    def copy(self):
        """
        Copy the current metaheuristic
        :return: Metaheuristic -- new Metaheuristic instance with the same properties
        """
        return self.__copy__()

    def __str__(self)->str:
        """
        String representation of the VnsOptimizer instance
        :return: string representation of the VnsOptimizer instance
        """
        s = super().__str__()
        return s;

    def __repr__(self)->str:
        """
        String representation of the VnsOptimizer instance
        :return: string representation of the VnsOptimizer instance
        """
        s = super().__repr__()
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the VnsOptimizer instance
        :param spec: str -- Format specification 
        :return: formatted VnsOptimizer instance
        """
        s = super().__format__(spec)
        return s