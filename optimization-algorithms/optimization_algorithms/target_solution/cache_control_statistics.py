class CacheControlStatistics:
    
    """
    Cache that is used during evaluation for previously obtained solutions
    """
    cache:dict = {}
    
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
