from pathlib import Path
import sys 
path = Path().joinpath().joinpath('..')
sys.path.append(str(path))

from abc import ABC, abstractmethod

from target_solution.cache_control_statistics import CacheControlStatistics

class TargetSolution(ABC):
    
    """
    Cache that is used during evaluation for previously obtained solutions
    """
    cache_control_statistics:CacheControlStatistics = CacheControlStatistics()
    
    @abstractmethod
    def __init__(self, name:str, fitness_value:float=None, objective_value:float=None, is_feasible:bool=False)->None:
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
        return TargetSolution(self.__name, self.__fitness_value, self.__objective_value)

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
        destination.name = self.name
        destination.fitness_value = self.fitness_value
        destination.objective_value = self.objective_value
        destination.is_feasible = self.is_feasible

    @property
    def name(self)->str:
        """
        Property getter for the name of the target solution
        :return: name of the target solution instance 
        """
        return self.__name

    @property
    def fitness_value(self)->float:
        """
        Property getter for fitness value of the target solution
        :return: fitness value of the target solution instance 
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
        :return: objective value of the target solution instance 
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
        :return: feasibility of the target solution instance 
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
        :return: solution code 
        """
        pass

    @abstractmethod
    def calculate_fitness(self)->float:
        """
        Fitness calculation of the target solution
        :return: target solution fitness value 
        """
        pass

    @abstractmethod
    def recalculate_solution_code(self)->None:
        """
        Recalculation of the solution code for the target solution
        """
        pass

    @abstractmethod
    def random_init(self)->None:
        """
        Random initialization of the target solution
        """
        pass

    @staticmethod
    def calculate_fitness_try_consult_cache(target_solution):
        """
        Calculate fitness of the argument with optional cache consultation
        :param target_solution:TargetSolution -- target solution whose fitness should be 
        :return: solution with calculated fitness value 
        """
        ccs = target_solution.cache_control_statistics 
        ccs.fitness_calculations_count += 1
        if ccs.is_caching:
            code = target_solution.solution_code()
            if code in ccs.cache:
                ccs.cache_hit_count += 1
                return ccs.cache[code]
            target_solution.fitness_value = target_solution.calculate_fitness()
            ccs.cache[code] = target_solution
            return target_solution
        else:
            target_solution.fitness_value = target_solution.calculate_fitness()
            return target_solution

    def evaluate(self)->None:
        """
        Evaluate current target solution
        """        
        solution = TargetSolution.calculate_fitness_try_consult_cache(self)
        self.objective_value = solution.objective_value;
        self.fitness_value = solution.fitness_value;
        self.feasible = solution.feasible;

    @abstractmethod
    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        """
        Calculate distance between two solutions determined by its code
        :param solution_code_1:str -- solution code for the first solution
        :param solution_code_2:str -- solution code for the second solution
        """
        pass

    def string_representation( self, delimiter:str)->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- Delimiter between fields
        :return: tring representation of target solution instance
        """        
        s = 'name= '+ self.name + delimiter
        s += 'fitness_value= '+ str(self.fitness_value) + delimiter
        s += 'objective_value= '+ str(self.objective_value) + delimiter
        s += 'is_feasible= '+ str(self.is_feasible) + delimiter
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the target solution instance
        :return: string representation of the target solution instance
        """
        return self.string_representation('| ')

    @abstractmethod
    def __repr__(self)->str:
        """
        Representation of the target solution instance
        :return: string representation of the solution instance
        """
        return self.string_representation('\n')

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the target solution instance
        :param spec: str -- Format specification
        :return: formatted target solution instance
        """
        return self.string_representation('| ')
