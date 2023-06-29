class EvaluationCacheControlStatistics:
    
    """
    Cache that is used during evaluation for previously obtained solutions
    """
    cache:dict[str] = {}
    
    """
    If caching is used during evaluation, or not
    """
    is_caching:bool = False

    """
    If caching is used during evaluation, cache hit is counted
    """
    cache_hit_count:int = 0

    """
    number of fitness calculations that is counted
    """
    fitness_calculations_count:int = 0

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
        for i in range(0, indentation-1):
            s += indentation_start      
        s += 'is_caching=' + str(self.is_caching) + delimiter
        s += 'cache_hit_count=' + str(self.cache_hit_count) + delimiter
        s += 'fitness_calculations_count=' + str(self.fitness_calculations_count) 
        for i in range(0, indentation-1):
            s += indentation_end 
        return s
