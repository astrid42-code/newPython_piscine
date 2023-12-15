def callLimit(limit: int):
    '''function that takes as argument a call limit of another function
    and blocks its execution above a limit.'''
    
    count = 0
    def callLimiter(function):
    def limit_function(*args: Any, **kwds: Any):
    #your code here
