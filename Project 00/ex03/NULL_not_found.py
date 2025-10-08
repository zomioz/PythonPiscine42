def NULL_not_found(object: any)-> int:

    type_names = {
        "<class 'NoneType'>": "None",
        "<class 'float'>": "nan",
        "<class 'int'>": "0",
        "<class 'str'>": "",
        "<class 'bool'>": "False"
    }

    object_type = str(type(object))
    type_names_key = type_names.keys()
    
    if object_type in type_names_key:
        tmp = str(object)
        if tmp == type_names[object_type]:
            print(":", type_names[object_type], object_type)
            return 0
        else:
            print("Type not Found")
            return 1
    else:
        print("Type not Found")
        return 1