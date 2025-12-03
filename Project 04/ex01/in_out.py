def square(x: int | float) -> int | float:

    '''
    Function that return a square of a number
    Argument: int or float
    Return: int or float
    '''

    return x * x


def pow(x: int | float) -> int | float:

    '''
    Function that return a power of a number
    Argument: int or float
    Return: int or float
    '''

    return x ** x


def outer(x: int | float, function) -> object:

    '''
    Function that apply a function pointer to a number
    Argument: a number, and a function
    Return: an object on inner function
    '''

    count = 0

    def inner() -> float:

        '''
        Function that use nonlocal variable to calculate iteration
        Argument: None
        Return: a float
        '''

        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count

    return inner
