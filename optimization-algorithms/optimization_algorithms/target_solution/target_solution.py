import path
import sys 

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent)

from copy import deepcopy
from collections import namedtuple
from abc import ABCMeta, abstractmethod

from target_problem.target_problem import TargetProblem
from target_solution.evaluation_cache_control_statistics import EvaluationCacheControlStatistics

ObjectiveFitnessFeasibility = namedtuple('ObjectiveFitnessFeasibility', ['objective_value', 
                'fitness_value', 
                'is_feasible'])

class TargetSolution(metaclass=ABCMeta):
    
    """
    Cache that is used during evaluation for previously obtained solutions
    """
    evaluation_cache_cs:EvaluationCacheControlStatistics = EvaluationCacheControlStatistics()
    
    @abstractmethod
    def __init__(self, name:str, fitness_value:float, objective_value:float, is_feasible:bool)->None:
        """
        Create new TargetSolution instance
        :param name:str -- name of the target solution
        :param fitness_value:float -- fitness value of the target solution
        :param objective_value:float -- objective value of the target solution
        """
        self.__name = name
        self.__fitness_value = fitness_value
        self.__objective_value = objective_value
        self.__is_feasible = is_feasible

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current target solution
        :return: TargetSolution -- new TargetSolution instance with the same properties
        """
        ts = deepcopy(self)
        return ts

    @abstractmethod
    def copy(self):
        """
        Copy the current target solution
        :return: TargetSolution -- new TargetSolution instance with the same properties
        """
        return self.__copy__()

    @abstractmethod
    def copy_to(self, destination)->None:
        """
        Copy the current target solution to the already existing destination target solution
        :param destination:TargetSolution -- destination target solution
        """
        destination =  copy(self)

    @property
    def name(self)->str:
        """
        Property getter for the name of the target solution
        :return: str -- name of the target solution instance 
        """
        return self.__name

    @property
    def fitness_value(self)->float:
        """
        Property getter for fitness value of the target solution
        :return: float -- fitness value of the target solution instance 
        """
        return self.__fitness_value

    @fitness_value.setter
    def fitness_value(self, value:float)->None:
        """
        Property setter for fitness value of the target solution
        """
        if value < 0:
            raise ValueError("Fitness value less than 0 is not possible.")
        self.__fitness_value = value

    @property
    def objective_value(self)->float:
        """
        Property getter for objective value of the target solution
        :return: float -- objective value of the target solution instance 
        """
        return self.__objective_value

    @objective_value.setter
    def objective_value(self, value:float)->None:
        """
        Property setter for objective value of the target solution
        """
        self.__objective_value = value

    @property
    def is_feasible(self)->bool:
        """
        Property getter for feasibility of the target solution
        :return: bool -- feasibility of the target solution instance 
        """
        return self.__is_feasible

    @is_feasible.setter
    def is_feasible(self, value:bool)->None:
        """
        Property setter for feasibility of the target solution
        """
        self.__is_feasible = value

    @abstractmethod
    def solution_code(self)->str:
        """
        Solution code of the target solution
        :return: str -- solution code 
        """
        raise NotImplementedError

    @abstractmethod
    def calculate_objective_fitness_feasibility(self, problem:TargetProblem)->ObjectiveFitnessFeasibility:
        """
        Fitness calculation of the target solution
        :param problem:TargetProblem -- problem that is solved
        :return: ObjectiveFitnessFeasibility -- objective value, fitness value and feasibility of the solution instance 
        """
        raise NotImplementedError

    @abstractmethod
    def recalculate_solution_code(self)->None:
        """
        Recalculation of the solution code for the target solution
        """
        raise NotImplementedError

    @abstractmethod
    def random_init(self)->None:
        """
        Random initialization of the target solution
        """
        raise NotImplementedError

    @staticmethod
    def calculate_objective_fitness_feasibility_try_consult_cache(target_solution, target_problem:TargetProblem):
        """
        Calculate fitness of the argument with optional cache consultation
        :param target_solution:TargetSolution -- target solution whose fitness should be 
        :param target_problem:TargetProblem -- problem that is solved
        :return: TargetSolution -- solution with calculated objection value, fitness value and feasibility
        """
        eccs = target_solution.evaluation_cache_cs 
        eccs.cache_request_count += 1
        if eccs.is_caching:
            code = target_solution.solution_code()
            if code in eccs.cache:
                eccs.cache_hit_count += 1
                return eccs.cache[code]
            triplet:ObjectiveFitnessFeasibility = target_solution.calculate_objective_fitness_feasibility(
                    target_problem)
            target_solution.objective_value = triplet.objective_value
            target_solution.fitness_value = triplet.fitness_value
            target_solution.is_feasible = triplet.is_feasible
            eccs.cache[code] = target_solution
            return target_solution
        else:
            triplet:ObjectiveFitnessFeasibility = target_solution.calculate_objective_fitness_feasibility(
                    target_problem)
            target_solution.objective_value = triplet.objective_value
            target_solution.fitness_value = triplet.fitness_value
            target_solution.is_feasible = triplet.is_feasible
            return target_solution

    def evaluate(self, target_problem:TargetProblem)->None:
        """
        Evaluate current target solution
        :param target_problem:TargetProblem -- problem that is solved
        """        
        solution = TargetSolution.calculate_objective_fitness_feasibility_try_consult_cache(self, target_problem)
        self.objective_value = solution.objective_value;
        self.fitness_value = solution.fitness_value;
        self.is_feasible = solution.is_feasible;

    @abstractmethod
    def best_1_change(self, problem:TargetProblem)->bool:
        """
        Change the best one within solution 
        :param problem:TargetProblem -- problem that is solved
        :return: bool -- if the best one is changed, or not
        """        
        raise NotImplementedError

    @abstractmethod
    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        """
        Calculate distance between two solutions determined by its code
        :param solution_code_1:str -- solution code for the first solution
        :param solution_code_2:str -- solution code for the second solution
        """
        raise NotImplementedError

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
        for i in range(0, indentation):
            s += indentation_symbol     
        s += 'name=' + self.name + delimiter
        for i in range(0, indentation):
            s += indentation_symbol     
        s += 'fitness_value=' + str(self.fitness_value) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol     
        s += 'objective_value=' + str(self.objective_value) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol     
        s += 'is_feasible=' + str(self.is_feasible) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol     
        s += 'solution_code=' + self.solution_code() + delimiter
        for i in range(0, indentation):
            s += indentation_symbol     
        s += 'evaluation_cache_cs=' + self.evaluation_cache_cs.string_representation(
                delimiter, indentation+1, indentation_symbol, '{', '}')  
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the target solution instance
        :return: str -- string representation of the target solution instance
        """
        return self.string_representation('|')

    @abstractmethod
    def __repr__(self)->str:
        """
        Representation of the target solution instance
        :return: str -- string representation of the target solution instance
        """
        return self.string_representation('\n')

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the target solution instance
        :param spec: str -- format specification
        :return: str -- formatted target solution instance
        """
        return self.string_representation('|')

