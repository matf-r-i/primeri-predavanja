from pathlib import Path
import sys 
path = Path().joinpath().joinpath('..')
sys.path.append(str(path))

from abc import ABCMeta, abstractmethod

from datetime import datetime

from target_problem.target_problem import TargetProblem

class Algorithm(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, name:str, is_minimization:bool, evaluations_max:int=0, seconds_max:int=0, target_problem:TargetProblem=None)->None:
        """
        Create new Algorithm instance
        :param name:str -- name of the algorithm
        :param is_minimization:bool -- is minimum is seek for
        :param evaluations_max:int -- maximum number of evaluations for algorithm execution
        :param seconds_max:int -- maximum number of seconds for algorithm execution
        :param target_problem:TargetProblem -- problem to be solved
        """
        self.__name = name
        self.__is_minimization = is_minimization
        self.__evaluations_max = evaluations_max
        self.__seconds_max = seconds_max
        self.__target_problem = target_problem
        self.__evaluation = 0
        self.__execution_started = None
        self.__execution_ended = None

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current algorithm
        :return: Algorithm -- new Algorithm instance with the same properties
        """
        return Algorithm(self.__name, self.__is_minimization, self.__evaluations_max, self.__seconds_max, self.__target_problem)

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
    def is_minimization(self)->bool:
        """
        Property getter for the name of the algorithm
        :return: bool -- if minimization takes place 
        """
        return self.__is_minimization

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
        :return: datetime -- When execution started 
        """
        return self.__execution_started

    @execution_started.setter
    def execution_started(self, value:datetime)->None:
        """
        Property setter for time when execution started
        :param value:datetime -- Time when execution started
        """
        self.__execution_started = value

    @property
    def execution_ended(self)->datetime:
        """
        Property getter for time when execution ended
        :return: datetime -- When execution ended 
        """
        return self.__execution_ended

    @execution_ended.setter
    def execution_ended(self, value:datetime)->None:
        """
        Property setter for time when execution ended
        :param value:datetime -- Time when execution ended
        """
        self.__execution_ended = value

    def string_representation(self, delimiter:str, indentation:int=0, indentation_start:str ='{', 
        indentation_end:str ='}')->str:
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
        s += 'name=' + self.name + delimiter
        s += 'is_minimization=' + str(self.is_minimization) + delimiter
        s += 'evaluations_max=' + str(self.evaluations_max) + delimiter
        s += 'target_problem={' + str(self.target_problem) + '}' + delimiter 
        s += '__evaluation=' + str(self.__evaluation) + delimiter
        s += 'execution_started=' + str(self.execution_started) + delimiter
        s += 'execution_ended=' + str(self.execution_ended) 
        for i in range(0, indentation):
            s += indentation_end 
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
        :param spec: str -- Format specification
        :return: str -- formatted algorithm instance
        """
        return self.string_representation('|')
