class Error(Exception):
    """Base class for exceptions.
    Attributes:
        -- expression: input expression in which the error occurred
        -- message: explanation of the error."""
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return repr(self.message)

class IncorrectType(Error):
    #User-supplied year is not an integer.
    pass

class OutOfRange(Error):
    #User-supplied year is not within the correct range.
    pass
        