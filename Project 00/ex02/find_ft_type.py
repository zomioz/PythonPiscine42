def all_thing_is_obj(object):

    ft_dict = {
        "<class 'list'>": "List",
        "<class 'tuple'>": "Tuple",
        "<class 'set'>": "Set",
        "<class 'dict'>": "Dict",
        "<class 'str'>": "is in the kitchen",
        "<class 'int'>": 'Int',
        "<class 'float'>": 'Float',
        "<class 'bool'>": 'Bool',
        "<class 'NoneType'>": 'NoneType'
    }

    tmp = str(type(object))
    key_list = ft_dict.keys()

    if tmp in key_list:

        if ft_dict[tmp] == "is in the kitchen":
            print(object, ft_dict[tmp], ":", type(object))
        else:
            print(ft_dict[tmp], ":", type(object))

    else:
        print("No type found")
    
    return 42