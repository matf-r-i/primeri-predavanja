class SolutionCodeDistanceCacheControlStatistics:

    def __init__(self, is_caching:bool=False, hit_count:int=0, requests_count:int=0, cache:dict[dict[str]]={})->None:
        """
        Create new cache, control and statistics for solution code distance calculation instance
        :param is_caching:bool -- if caching will be applied during calculation of the solution code distances
        :param hit_count:int -- count of the cache hits
        :param requests_count:int -- count of the overall cache requests 
        :param cache:dict -- cache that stores distances among solution codes
        """
        self.__is_caching = is_caching
        self.__hit_count = hit_count
        self.__requests_count = requests_count
        self.__cache = cache

    def __copy__(self):
        """
        Internal copy of the current cache, control and statistics for solution code distance calculation
        :return: SolutionCodeDistanceCacheControlStatistics -- new cache, control and statistics for solution code distance calculation
        """
        scd_ccs = SolutionCodeDistanceCacheControlStatistics(self.__is_caching, self.__hit_count, self.__requests_count, self.__cache)
        return scd_ccs

    def copy(self):
        """
        Copy the current cache, control and statistics for solution code distance calculation
        :return: SolutionCodeDistanceCacheControlStatistics -- new cache, control and statistics for solution code distance calculation with the same properties
        """
        return self.__copy__()

    def copy_to(self, destination)->None:
        """
        Copy the current cache, control and statistics for solution code distance calculation to the already existing destination instance
        :param destination:SolutionCodeDistanceCacheControlStatistics -- destination cache, control and statistics for solution code distance calculation
        """
        destination.is_caching = self.is_caching
        destination.hit_count = self.hit_count
        destination.requests_count = self.requests_count
        destination.cache = self.cache

    @property
    def is_caching(self)->bool:
        """
        Property getter for checking if caching is activated
        :return: bool -- if caching is activated 
        """
        return self.__is_caching

    @is_caching.setter
    def is_caching(self, value:bool)->None:
        """
        Property setter for info if caching is activated
        """
        self.__is_caching = value

    @property
    def hit_count(self)->int:
        """
        Property getter for cache hit count 
        :return: int -- cache hit count 
        """
        return self.__hit_count

    @hit_count.setter
    def hit_count(self, value:int)->None:
        """
        Property setter for hit count
        """
        self.__hit_count = value

    @property
    def requests_count(self)->int:
        """
        Property getter for cache requests count 
        :return: int -- cache requests count 
        """
        return self.__requests_count

    @requests_count.setter
    def requests_count(self, value:int)->None:
        """
        Property setter for requests count
        """
        self.__requests_count = value

    @property
    def cache(self)->dict:
        """
        Property getter for cache 
        :return: dict -- cache  
        """
        return self.__cache

    @cache.setter
    def cache(self, value:int)->None:
        """
        Property setter for cache
        """
        self.__cache = value

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
        s += 'cache_hit_count=' + str(self.hit_count) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'cache_requests_count=' + str(self.requests_count) + delimiter
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


