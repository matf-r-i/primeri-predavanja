import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import copy

from random import random

from bitstring import BitArray

from utils.logger import logger

from target_problem.target_problem import TargetProblem

from target_solution.target_solution import TargetSolution

from algorithm.metaheuristic.variable_neighborhood_search.target_solution_vns_support import TargetSolutionVnsSupport

from max_ones_problem import MaxOnesProblem

class MaxOnesSolution(TargetSolution):
    
    def __init__(self, problem:MaxOnesProblem=None)->None:
        """
        Create new MaxOnesSolution instance
        """
        super().__init__("MaxOnesSolution")
        self.__problem = copy.copy(problem)
        self.__representation:BitArray = BitArray()

    def __copy__(self):
        """
        Internal copy of the MaxOnesSolution problem
        :return: MaxOnesSolution -- new MaxOnesSolution instance with the same properties
        """
        sol = MaxOnesSolution()
        sol.__problem = copy.copy(self.__problem)
        sol.__representation = self.__representation
        return sol

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

    @property
    def representation(self)->BitArray:
        """
        Property getter for the target solution representation
        :return: BitArray -- the target solution instance representation
        """
        return self.__representation

    @representation.setter
    def representation(self, value:BitArray)->None:
        """
        Property setter for representation of the target solution
        :param value:BitArray -- representation of the target solution
        """
        self.__representation = value

    @property
    def problem(self)->MaxOnesProblem:
        """
        Property getter for the solution's problem
        :return: MaxOnesProblem -- the solution's problem
        """
        return self.__problem

    @representation.setter
    def problem(self, value:MaxOnesProblem)->None:
        """
        Property setter for solution's problem
        :param value:MaxOnesProblem -- the target solution's problem
        """
        self.__problem = value

    def random_init(self)->None:
        """
        Random initialization of the target solution
        """
        logger.debug( "Solution:\n" + str(self))
        self.representation = BitArray(self.problem.dimension)
        for i in range(self.problem.dimension):
            if random() > 0.5:
                self.representation[i] = True
            else:
                self.representation[i] = False


    def solution_code(self)->str:
        """
        Solution code of the target solution
        :return: str -- solution code 
        """
        return str(self.representation)

    def calculate_fitness(self)->float:
        """
        Fitness calculation of the max ones solution
        :return: float -- fitness value of the current solution 
        """
        fit = 0
        return fit


    def recalculate_solution_code(self)->None:
        """
        Recalculation of the solution code for the target solution
        """
        raise NotImplementedError('recalculate_solution_code')

    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        """
        Calculating distance between two solutions determined by its code
        :param solution_code_1:str -- solution code for the first solution
        :param solution_code_2:str -- solution code for the second solution
        """
        raise NotImplementedError('solution_code_distance')

    def best_1_change(self)->bool:
        """
        Change the best one within solution 
        :return: bool -- if the best one is changed, or not
        """        
        raise NotImplementedError('best_1_change')

    def randomize(k:int, solution_codes:list[str])->bool:
        """
        Randomizes solution codes 
        :param k:int -- parameter for VNS
        :param solution_codes:list[str] -- solution codes that should be randomized
        :return: bool -- if randomization is successful 
        """    
        raise NotImplementedError('randomize')


    def string_representation(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
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
        s += group_start
        s += super().string_representation(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += problem.string_representation(delimiter, indentation+1, '', '{', '}')
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the target solution instance
        :return: str -- string representation of the target solution instance
        """
        return self.string_representation('|', 0, '', '{', '}')

    def __repr__(self)->str:
        """
        Representation of the target solution instance
        :return: str -- string representation of the solution instance
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        """
        Formatted the target solution instance
        :param spec: str -- format specification
        :return: str -- formatted target solution instance
        """
        return self.string_representation('|')

