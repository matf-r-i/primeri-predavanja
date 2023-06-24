import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from target_problem import TargetProblemMaxOnes

# print ("aaa")

problem = TargetProblemMaxOnes("aaa")
print(problem)
