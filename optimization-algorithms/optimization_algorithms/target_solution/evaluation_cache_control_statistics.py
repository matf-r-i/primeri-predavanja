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

    def string_representation(self, delimiter:str)->str:
        """
        String representation of the cache control and statistics structure
        :param delimiter: str -- Delimiter between fields
        :return: str -- string representation of cache control and statistics structure
        """        
        s = 'is_caching=' + str(self.is_caching) + delimiter
        s += 'cache_hit_count=' + str(self.cache_hit_count) + delimiter
        s += 'fitness_calculations_count=' + str(self.fitness_calculations_count) 
        return s
