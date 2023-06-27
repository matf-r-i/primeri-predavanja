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
        Internal copy of the current VnsOptimizer
        :return: VnsOptimizer -- new VnsOptimizer instance with the same properties
        """
        return VnsOptimizer(self.__name, self.__is_minimization, self.__evaluations_max)

    def copy(self):
        """
        Copy the current VnsOptimizer instance
        :return: VnsOptimizer -- new VnsOptimizer instance with the same properties
        """
        return self.__copy__()

    def string_representation(self, delimiter:str)->str:
        """
        String representation of the VnsOptimizer instance
        :param delimiter: str -- Delimiter between fields
        :return: string representation of VnsOptimizer instance
        """        
        s = super().string_representation(delimiter)
        return s

    def __str__(self)->str:
        """
        String representation of the VnsOptimizer instance
        :return: string representation of the VnsOptimizer instance
        """
        s = self.string_representation('|')
        return s;

    def __repr__(self)->str:
        """
        String representation of the VnsOptimizer instance
        :return: string representation of the VnsOptimizer instance
        """
        s = self.string_representation('\n')
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the VnsOptimizer instance
        :param spec: str -- Format specification 
        :return: formatted VnsOptimizer instance
        """
        s = self.string_representation('|')
        return s