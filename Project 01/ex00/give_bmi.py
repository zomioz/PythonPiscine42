def check_arg_bmi(height: list[int | float], weight: list[int | float]) \
                                                                -> bool:

    '''
    check argument of create_bmi(), type of argument and length of the two list
    Argument: two list of int or float
    Return: a bool, True on succes, False on fail
    '''

    len_height = len(height)
    len_weight = len(weight)

    if len_height != len_weight:
        return False

    for x in height + weight:
        if not isinstance(x, (int, float)):
            return False
        if x <= 0:
            return False

    return True


def create_bmi(height: list[int | float], weight: list[int | float]) \
                                            -> list[int | float]:

    '''
    Funciton to create a new list of BMI from hei and wei
    Argument: two list of int or float
    Return: a new list of in or float that contain BMI
    '''

    bmi_list = []

    for x in range(len(height)):
        bmi = weight[x] / (height[x] ** 2)
        bmi_list.append(bmi)

    return bmi_list


def give_bmi(height: list[int | float], weight: list[int | float]) \
                                                -> list[int | float]:

    '''
    Funciton that create a list of BMI
    Argument: two list of int or float that contain height and weight
    Return: a list of int or float that contain BMI
    '''

    if not check_arg_bmi(height, weight):
        print("Error give_bmi : list must be int or float \
        greater than 0, and the same lenght")
        return []

    bmi_list = create_bmi(height, weight)
    return bmi_list


def check_arg_limit(bmi: list[int | float], limit: int) -> bool:

    '''
    Function to check argument from apply_limit, check the type
    Argument: a list of int or float, and the limit in a int
    Return: a bool, True on succes, False on fail
    '''

    if type(limit) != int:
        print("Error apply_limit : Argument \
        must be list of int or float, and an int")
        return False

    for x in bmi:
        if not isinstance(x, (int, float)):
            print("Error apply_limit : Argument must be \
            list of int or float, and an int")
            return False

    return True


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    '''
    Function to apply a limit on a list of int or float
    Argument: a list of int or float, and the limit in a int
    Return: a list of bool for each case
    '''

    if not check_arg_limit(bmi, limit):
        return []

    bmi_limit = []

    for x in range(len(bmi)):
        if bmi[x] > limit:
            bmi_limit.append(True)
        else:
            bmi_limit.append(False)

    return bmi_limit
