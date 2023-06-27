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
        Copy the MaxOnesSolution
        :return: MaxOnesSolution -- new MaxOnesSolution instance with the same properties
        """
        return self.__copy__()
        
    def copy_to(self, destination)->None:
        """
        Copy the MaxOnesSolution to the already existing destination MaxOnesSolution
        :param destination:MaxOnesSolution -- destination MaxOnesSolution
        """
        return self.copy_to(destination)
        
    def solution_code(self)->str:
        """
        Solution code of the target solution
        :return: solution code 
        """
        return 'XXX'

    def calculate_fitness(self)->float:
        """
        Fitness calculation of the target solution
        :return: target solution fitness value 
        """
        return 0

    def recalculate_solution_code(self)->None:
        """
        Recalculation of the solution code for the target solution
        """
        pass

    def random_init(self)->None:
        """
        Random initialization of the target solution
        """
        pass

    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        """
        Calculating distance between two solutions determined by its code
        :param solution_code_1:str -- solution code for the first solution
        :param solution_code_2:str -- solution code for the second solution
        """
        return 0

    def best_1_change(self)->bool:
        """
        Change the best one within solution 
        :return: bool -- if the best one is changed, or not
        """        
        return False


    def string_representation(self, delimiter:str)->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- Delimiter between fields
        :return: string representation of target solution instance
        """        
        s = super().string_representation(delimiter)
        return s

    def __str__(self)->str:
        """
        String representation of the target solution instance
        :return: string representation of the target solution instance
        """
        return self.string_representation('|')

    def __repr__(self)->str:
        """
        Representation of the target solution instance
        :return: string representation of the solution instance
        """
        return self.string_representation('\n')

    def __format__(self, spec:str)->str:
        """
        Formatted the target solution instance
        :param spec: str -- Format specification
        :return: formatted target solution instance
        """
        return self.string_representation('|')
