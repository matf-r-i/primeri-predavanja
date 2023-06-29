import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from typing import Dict, TypeVar, Generic

from metaheuristic import Metaheuristic

from target_problem.target_problem import TargetProblem

from target_solution.target_solution import TargetSolution

from algorithm.metaheuristic.variable_neighborhood_search.target_solution_vns_support import TargetSolutionVnsSupport

S_co = TypeVar("S_co", covariant=True, bound=TargetSolution) # and bound by TargetSolutionVnsSupport 

class VnsOptimizer(Metaheuristic, Generic[S_co]):
    
    def __init__(self, is_minimization:bool, evaluations_max:int=0, seconds_max:int=0, random_seed:int=0, 
        target_problem:TargetProblem=None, initial_solution:S_co=None, k_min:int=1, k_max:int=3, 
                max_local_optima:int=1)->None:
        """
        Create new VnsOptimizer instance
        :param is_minimization:bool -- is minimum is seek for
        :param evaluations_max:int -- maximum number of evaluations for algorithm execution
        :param seconds_max:int -- maximum number of seconds for algorithm execution
        :param random_seed:int -- random seed for metaheuristic execution
        :param target_problem:TargetProblem -- problem to be solved
        :param initial_solution:S -- initial solution of the problem that is optimized by VNS 
        :param k_min:int -- k_min parameter for VNS
        :param k_max:int -- k_max parameter for VNS
        :param max_local_optima:int -- max_local_optima parameter for VNS
        """
        super().__init__('vns', is_minimization, evaluations_max, seconds_max, random_seed, target_problem)
        self.__current_solution:S_co = initial_solution
        self.__k_min = k_min
        self.__k_max = k_max
        self.__max_local_optima = max_local_optima
        self.__local_optima:Dict[str, float] = {}

    def __copy__(self):
        """
        Internal copy of the current VnsOptimizer
        :return: VnsOptimizer -- new VnsOptimizer instance with the same properties
        """
        return VnsOptimizer(self.__name, self.__is_minimization, self.__evaluations_max, self.__target_problem)

    def copy(self):
        """
        Copy the current VnsOptimizer instance
        :return: VnsOptimizer -- new VnsOptimizer instance with the same properties
        """
        return self.__copy__()

    @property
    def current_solution(self)->S_co:
        """
        Property getter for the current solution used during VNS execution
        :return: instance of the TargetSolution class subtype -- current solution of the problem 
        """
        return self.__current_solution

    @property
    def k_min(self)->int:
        """
        Property getter for the k_min parameter for VNS
        :return: int -- k_min parameter for VNS 
        """
        return self.__k_min

    @property
    def k_max(self)->int:
        """
        Property getter for the k_max parameter for VNS
        :return: int -- k_max parameter for VNS 
        """
        return self.__k_max

    def init(self)->None:
        """
        Initialization of the VNS algorithm
        """
        self.__k_current = self.k_min
        self.current_solution.evaluate();
        self.copy_to_best_solution(self.current_solution);

    def __shaking__(self)->bool:
        """
        Shaking phase of the VNS algorithm
        :return: bool -- if shaking is succesfull 
        """
        """
        private bool Shaking()
        {
            var shakingPoints = SelectShakingPoints();
            if (shakingPoints == null)
            {
                Log.Debug("it: {0}\ttime: {1:0}s\tm: {2}\tk: {3}\tSkipping"/*\tbestSolCode: {9}"*/, iteration, ElapsedSeconds(), mCurrent, kCurrent);
                return false;
            }
            if (!currentSolution.Randomize(kCurrent, shakingPoints))
                return false;
            var km = new KeyValuePair<int, double>(mCurrent, kCurrent);
            if (shakingCounts.ContainsKey(km))
                shakingCounts[km]++;
            else
                shakingCounts[km] = 1;
            iteration++;
            evaluation++;
            currentSolution.Evaluate();
            currentSolution.LocalSearchBestImprovement();
            PrintStatus(currentSolution);

            //remembering whole history - only informative, not used in algorithm search decision making - therefore, it can be disabled if memory is issue
            allSolutionCodes.Add(currentSolution.SolutionCode());
            //we do not need to enter this in case of classic VNS - it uses randomness so it messes with randgen so for different maxLocalOptima and mMax=0 gives different results which is confusing
            if (mMax > 0 && !AddLocalOptima(currentSolution))
                return false;

            bool? newBetter = FirstSolutionBetter(currentSolution, bestSolution);
            if (!newBetter.HasValue)
            {
                Log.Debug("Same solution quality, generating random true with probability 0.5");
                return RandomNumbers.NextDouble() < 0.5;
            }
            if (newBetter.Value)
            {
                //new best
                if (improvementCounts.ContainsKey(km))
                    improvementCounts[km]++;
                else
                    improvementCounts[km] = 1;
                improvementChronology.Add(iteration - 1, km);
            }
            return newBetter.Value;
        }
        """


    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the VNS algorithm
        """
        while self.shaking():
            self.copy_to_best_solution(self.current_solution)
            self.__k_current = self.k_min
        if self.__k_current < self.k_max:
            self.__k_current += 1
        else:
            self.__k_current = self.k_min

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
        s = super().string_representation(delimiter)
        s += delimiter
        s += 'current_solution=' + self.current_solution.string_representation(delimiter=delimiter, 
                indentation=indentation+1) + delimiter 
        s += 'k_min=' + str(self.k_min) + delimiter 
        s += 'k_max=' + str(self.k_max) 
        for i in range(0, indentation):
            s += indentation_end 
        return s


    def __str__(self)->str:
        """
        String representation of the VnsOptimizer instance
        :return: str -- string representation of the VnsOptimizer instance
        """
        s = self.string_representation('|')
        return s;

    def __repr__(self)->str:
        """
        String representation of the VnsOptimizer instance
        :return: str -- string representation of the VnsOptimizer instance
        """
        s = self.string_representation('\n')
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the VnsOptimizer instance
        :param spec: str -- Format specification 
        :return: str -- formatted VnsOptimizer instance
        """
        s = self.string_representation('|')
        return s