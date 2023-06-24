import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from target_problem import TargetProblem

class TargetProblemMaxOnes(TargetProblem):
    def __init__(self, file_path:str ):
        """
        Create new TargetProblemMaxOnes instance
        :param file_path:str -- path of the file with data for the parget problem instance 
        """
        super(self, "TargetProblemMaxOnes", file_path)
