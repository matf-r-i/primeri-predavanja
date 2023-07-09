import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

class OutputControl:

    """
    If metaheuristic will write to output, or not
    """
    write_to_output:bool = False

    """
    Output file to which metaheuristic will write
    """
    output_file = None
    

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
        s += 'is_writing_to_output=' + str(self.is_writing_to_output) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'output_file=' + str(self.output_file) + delimiter
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


