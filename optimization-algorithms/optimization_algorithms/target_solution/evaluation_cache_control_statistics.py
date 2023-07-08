import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

class EvaluationCacheControlStatistics:

    """
    If caching is used during evaluation, or not
    """
    is_caching:bool = False

    """
    Cache that is used during evaluation for previously obtained solutions
    """
    cache:dict[str] = {}
    
    """
    If caching is used during evaluation, cache hit is counted
    """
    cache_hit_count:int = 0

    """
    number of fitness calculations that is counted
    """
    cache_request_count:int = 0

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
        s += 'is_caching=' + str(self.is_caching) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol      
        s += 'cache_hit_count=' + str(self.cache_hit_count) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol      
        s += 'cache_request_count=' + str(self.cache_request_count) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s
