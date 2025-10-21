def check_arg(family: list, start: int, end: int) -> bool:

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

    print("My", word, "is : (", end="")
    print(len(lst), end="")
    if len(lst) > 0:
        print(",", len(lst[0]), end="")
    else:
        print(", 0", end="")
    print(")")


def slice_me(family: list, start: int, end: int) -> list:

    if check_arg(family, start, end) == False:
        return []

    print_shape(family, "shape")
    new_family = family[start:end]
    print_shape(new_family, "new shape")
    return new_family