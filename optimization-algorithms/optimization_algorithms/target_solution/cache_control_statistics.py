class CacheControlStatistics:
    
    """
    Cache that is used during evaluation for previously obtained solutions
    """
    cache:dict = None
    
    """
    If caching is used during evaluation, or not
    """
    is_caching:bool = False

    """
    If caching is used during evaluation, cache hit is counted
    """
    cache_hit_count:int = 0

    """
    number of evaluations (eg. fitness calculations) that is counted
    """
    evaluation_count:int = 0
