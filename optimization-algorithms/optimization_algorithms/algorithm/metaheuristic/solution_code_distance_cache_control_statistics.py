import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

class SolutionCodeDistanceCacheControlStatistics:

    """
    If caching is used during calculation of the solution code distances, or not
    """
    is_caching:bool = False

    """
    Cache that is used during calculation for previously obtained solution code distances
    """
    cache:dict[dict[str]] = {}
    
    """
    If caching is used during calculation of the solution code distances, cache hit is counted
    """
    cache_hit_count:int = 0

    """
    overall number of calculation of the solution code distances
    """
    cache_request_count:int = 0

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of solution distance calculation cache control statistic 
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
        s += 'cache_requests_count=' + str(self.cache_request_count) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the cache control and statistics structure
        :return: str -- string representation of the cache control and statistics structure
        """
        return self.string_representation('|')

    def __repr__(self)->str:
        """
        Representation of the cache control and statistics structure
        :return: str -- string representation of cache control and statistics structure
        """
        return self.string_representation('\n')


    def __format__(self, spec:str)->str:
        """
        Formatted the cache control and statistics structure
        :param spec: str -- format specification
        :return: str -- formatted cache control and statistics structure
        """
        return self.string_representation('|')


