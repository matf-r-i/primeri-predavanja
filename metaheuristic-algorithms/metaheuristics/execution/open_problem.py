import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

from problems.max_ones.target_problem_max_ones import TargetProblemMaxOnes

# print ("aaa")

problem = TargetProblemMaxOnes("aaa")
print(problem)
