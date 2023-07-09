import path
import sys 

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from copy import deepcopy
from datetime import datetime
from abc import ABCMeta, abstractmethod

from utils.logger import logger
from target_problem.target_problem import TargetProblem

class Algorithm(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, name:str, evaluations_max:int, seconds_max:int, target_problem:TargetProblem)->None:
        """
        Create new Algorithm instance
        :param name:str -- name of the algorithm
        :param evaluations_max:int -- maximum number of evaluations for algorithm execution
        :param seconds_max:int -- maximum number of seconds for algorithm execution
        :param target_problem:TargetProblem -- problem to be solved
        """
        self.__name:str = name
        self.__evaluations_max:int = evaluations_max
        self.__seconds_max:int = seconds_max
        self.__target_problem:TargetProblem = target_problem
        self.__evaluation:int = 0
        self.__execution_started:datetime = None
        self.__execution_ended:datetime = None

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current algorithm
        :return: Algorithm -- new Algorithm instance with the same properties
        """
        alg = deepcopy(self)
        return alg

    @abstractmethod
    def copy(self):
        """
        Copy the current algorithm
        :return: Algorithm -- new Algorithm instance with the same properties
        """
        return self.__copy__()

    @property
    def name(self)->str:
        """
        Property getter for the name of the algorithm
        :return: str -- name of the algorithm instance 
        """
        return self.__name

    @property
    def evaluations_max(self)->int:
        """
        Property getter for the maximum number of evaluations for algorithm execution
        :return: int -- maximum number of evaluations 
        """
        return self.__evaluations_max

    @property
    def seconds_max(self)->int:
        """
        Property getter for the maximum number of seconds for algorithm execution
        :return: int -- maximum number of seconds 
        """
        return self.__seconds_max

    @property
    def target_problem(self)->TargetProblem:
        """
        Property getter for the target problem to be solved
        :return: TargetProblem -- target problem to be solved 
        """
        return self.__target_problem

    @property
    def evaluation(self)->int:
        """
        Property getter for current number of evaluations during algorithm execution
        :return: int -- current number of evaluations 
        """
        return self.__evaluation

    @evaluation.setter
    def evaluation(self, value:int)->None:
        """
        Property setter for current number of evaluations
        """
        self.__evaluation = value

    @property
    def execution_started(self)->datetime:
        """
        Property getter for time when execution started
        :return: datetime -- time when execution started 
        """
        return self.__execution_started

    @execution_started.setter
    def execution_started(self, value:datetime)->None:
        """
        Property setter for time when execution started
        :param value:datetime -- time when execution started
        """
        self.__execution_started = value

    @property
    def execution_ended(self)->datetime:
        """
        Property getter for time when execution ended
        :return: datetime -- time when execution ended 
        """
        return self.__execution_ended

    @execution_ended.setter
    def execution_ended(self, value:datetime)->None:
        """
        Property setter for time when execution ended
        :param value:datetime -- time when execution ended
        """
        self.__execution_ended = value

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
        s = group_start
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'name=' + self.name + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'evaluations_max=' + str(self.evaluations_max) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'target_problem=' + self.target_problem.string_representation(delimiter, indentation + 1, 
                indentation_symbol, '{', '}')  + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__evaluation=' + str(self.__evaluation) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'execution_started=' + str(self.execution_started) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'execution_ended=' + str(self.execution_ended) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s


    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the algorithm instance
        :return: str -- string representation of the algorithm instance
        """
        return self.string_representation('|')

    @abstractmethod
    def __repr__(self)->str:
        """
        Representation of the algorithm instance
        :return: str -- string representation of the problem instance
        """
        return self.string_representation('\n')

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the algorithm instance
        :param spec: str -- format specification
        :return: str -- formatted algorithm instance
        """
        return self.string_representation('|')
