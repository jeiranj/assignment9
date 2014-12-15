import re

def check_type(year):
    """Check type of user-supplied 'year'. 
       If not a number, it returns False.
       Args:
            -- year """
    if type(year) == str:
        year = year.strip()
        matches = bool(re.match('\d+',year))
        return matches
    else: 
        return False
    
def check_range(year,first,last):
    """Check range of user-supplied 'year'.
       If not in [first,last], it returns False.
       Args:
            -- year
            -- first
            -- last """
    year = int(year)
    first = int(first)
    last = int(last)
    if (year>=first) & (year<=last):  
        return True
    else: 
        return False