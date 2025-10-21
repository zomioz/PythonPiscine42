def check_arg(family: list, start: int, end: int) -> bool:

    '''
    A checker of argument, check length, type and protection
    Argument: a list, an int for start and end
    Return: Bool, True on succes, False on fail
    '''

    if type(start) != int or type(end) != int:
        print("Error: start and end must be int type")
        return False

    if type(family) != list:
        print("Error : Bad argument, Argument isn't list")
        return False
    
    if len(family) == 0:
        print("Error: Empty list")
        return False

    for x in family:
        if not isinstance(x , list):
            print("Error : All sublists must be list type")
            return False

    first_size = len(family[0])
    for x, sublist in enumerate(family):
        if len(sublist) != first_size:
            print("Error : All sublists must have the same size.")
            return False

    if start >= len(family) or start < 0:
        print("Error: start isn't in range of family")
        return False
    
    return True

def print_shape(lst: list, word: str) -> None:

    '''
    Function that print the old list and the new list
    Argument: the list to print, and a word for describe the list
    Return: None
    '''

    print("My", word, "is : (", end="")
    print(len(lst), end="")
    if len(lst) > 0:
        print(",", len(lst[0]), end="")
    else:
        print(", 0", end="")
    print(")")


def slice_me(family: list, start: int, end: int) -> list:

    '''
    Function that rlice a list from start to end
    Argument: a list, an int for start where the slice start, an int for end for where the new list end
    Return: a slice of the original list from start to end
    '''

    if check_arg(family, start, end) == False:
        return []

    print_shape(family, "shape")
    new_family = family[start:end]
    print_shape(new_family, "new shape")
    return new_family