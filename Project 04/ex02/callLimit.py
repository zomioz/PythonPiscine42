def callLimit(limit: int):

    '''
    Wrapper function to get the callLimit
    Argument: a int for max call
    Return: a object to a function
    '''

    count = 0

    def callLimiter(function):

        '''
        Apply a function to the wrapper
        Argument: a pointer to function
        Return: a object to a function
        '''

        def limit_function(*args: any, **kwds: any):

            '''
            Run function from callLimiter and apply the limit from the wrapper
            Argument: args and kwargs
            Return: Object on function or Error message
            '''

            nonlocal count
            if count < limit:
                count += 1
                function()
                return function
            else:
                return print("Error:", function, "call too many times")

        return limit_function

    return callLimiter
