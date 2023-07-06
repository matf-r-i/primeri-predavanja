import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from copy import deepcopy
from random import choice
from random import random
from bitstring import BitArray

from utils.logger import logger
from target_problem.target_problem import TargetProblem
from max_ones_problem import MaxOnesProblem
from target_solution.target_solution import ObjectiveFitnessFeasibility
from target_solution.target_solution import TargetSolution
from algorithm.metaheuristic.variable_neighborhood_search.target_solution_vns_support import TargetSolutionVnsSupport

class MaxOnesSolution(TargetSolution, TargetSolutionVnsSupport):
    
    def __init__(self, problem:MaxOnesProblem)->None:
        """
        Create new MaxOnesSolution instance
        """
        super().__init__("MaxOnesSolution", fitness_value=None, objective_value=None, is_feasible=False)
        self.__problem:MaxOnesProblem = problem
        self.__representation:BitArray = BitArray()

    def __copy__(self):
        """
        Internal copy of the MaxOnesSolution problem
        :return: MaxOnesSolution -- new MaxOnesSolution instance with the same properties
        """
        sol = MaxOnesSolution(deepcopy(self.__problem))
        sol.__representation = deepcopy(self.__representation)
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

    @problem.setter
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
        #logger.debug( "\nSolution: {}".format(self))
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
        s:str = ''
        for bit in self.representation:
            if bit:
                s += '1'
            else:
                s += '0'
        return s

    def calculate_fitness(self)->ObjectiveFitnessFeasibility:
        """
        Fitness calculation of the max ones solution
        :return: ObjectiveFitnessFeasibility -- objective value, fitness value and feasibility of the solution instance  
        """
        ones_count = 0
        for i in range(self.problem.dimension):
            if self.representation[i]:
                ones_count += 1
        return ObjectiveFitnessFeasibility(ones_count, ones_count, True)

    def __representation_string_to_bit_array__(self, representation_str:str)->BitArray:
        """
        Obtain BitArray representation from string representation
        :param representation_str:str -- solution's representation as string
        :return: BitArray -- solution's representation as BitArray
        """
        return BitArray(representation_str)

    def recalculate_solution_code(self)->None:
        """
        Recalculation of the solution code for the target solution
        """
        return

    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        """
        Calculating distance between two solutions determined by its code
        :param solution_code_1:str -- solution code for the first solution
        :param solution_code_2:str -- solution code for the second solution
        """
        rep_1:BitArray = self.__representation_string_to_bit_array__(solution_code_1)
        rep_2:BitArray = self.__representation_string_to_bit_array__(solution_code_1)
        result = (rep_1 ^ rep_2).count(True)
        return result 

    def best_1_change(self)->bool:
        """
        Change the best one within solution 
        :return: bool -- if the best one is changed, or not
        """        
        best_ind:int = None
        best_fv:float = self.fitness_value
        for i in range(0, len(self.representation)):
            self.representation.invert(i) 
            new_fv = self.calculate_fitness().fitness_value
            if new_fv > best_fv:
                best_ind = i
                best_fv = new_fv
            self.representation.invert(i)
        if best_ind is not None:
            self.representation.invert(best_ind)
            self.evaluate()
            if self.fitness_value != best_fv:
                raise Exception('Fitness calculation within best_1_change function is not correct.')
            return True
        return False

    def vns_randomize(self, k:int, solution_codes:list[str])->bool:
        """
        Random VNS shaking of k parts such that new solution code does not differ more than k from all solution codes 
        inside shakingPoints 
        :param k:int -- parameter for VNS
        :param solution_codes:list[str] -- solution codes that should be randomized
        :return: bool -- if randomization is successful 
        """    
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            positions:list[int] = []
            for i in range(0,k):
                positions.append(choice(range(k)))
            new_representation:BitArray = deepcopy(self.representation)
            for p in positions:
                new_representation.invert(p)
            all_ok:bool = True
            #logger.debug(solution_codes)
            for sc in solution_codes:
                sc_representation = self.__representation_string_to_bit_array__(sc)
                if sc_representation is not None and sc_representation != '':
                    comp_result:int = (sc_representation ^ new_representation).count(value=1)
                    if comp_result > k:
                        all_ok = False
            if all_ok:
                break
        if tries < limit:
            self.representation = new_representation
            self.evaluate()
            return True
        else:
            return False 
        
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
        s += 'problem=' + self.problem.string_representation(delimiter, indentation+1, indentation_symbol, '{', '}')
        s += delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'representation=' + str(self.__representation)
        s += delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the target solution instance
        :return: str -- string representation of the target solution instance
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

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
        return self.string_representation('\n', 0, '   ', '{', '}')

