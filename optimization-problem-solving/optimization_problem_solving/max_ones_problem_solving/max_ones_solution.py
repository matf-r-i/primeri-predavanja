import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from target_solution.target_solution import TargetSolution

from algorithm.metaheuristic.variable_neighborhood_search.target_solution_vns_support import TargetSolutionVnsSupport

class MaxOnesSolution(TargetSolution, TargetSolutionVnsSupport):
    
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
        :return: str -- solution code 
        """
        return 'XXX'

    def calculate_fitness(self)->float:
        """
        Fitness calculation of the target solution
        :return: float -- fitness value of the current solution 
        """
        return 0

    def recalculate_solution_code(self)->None:
        """
        Recalculation of the solution code for the target solution
        """
        return None

    def random_init(self)->None:
        """
        Random initialization of the target solution
        """
        return None

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

    def randomize(k:int, solution_codes:list[str])->bool:
        """
        Randomizes solution codes 
        :param k:int -- parameter for VNS
        :param solution_codes:list[str] -- solution codes that should be randomized
        :return: bool -- if randomization is successful 
        """    
        return False

    def string_representation(self, delimiter:str, indentation:int=0, indentation_start:str='{', 
            indentation_end:str='}',)->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- Delimiter between fields
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
        String representation of the target solution instance
        :return: str -- string representation of the target solution instance
        """
        return self.string_representation('|')

    def __repr__(self)->str:
        """
        Representation of the target solution instance
        :return: str -- string representation of the solution instance
        """
        return self.string_representation('\n')

    def __format__(self, spec:str)->str:
        """
        Formatted the target solution instance
        :param spec: str -- Format specification
        :return: str -- formatted target solution instance
        """
        return self.string_representation('|')
