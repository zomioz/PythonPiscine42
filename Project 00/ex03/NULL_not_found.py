def NULL_not_found(object: any)-> int:

    type_names = {
        "<class 'NoneType'>": "Nothing",
        "<class 'float'>": "Cheese",
        "<class 'int'>": "Zero",
        "<class 'str'>": "Empty",
        "<class 'bool'>": "Fake"
    }

    object_type = str(type(object))
    type_names_key = type_names.keys()
    
    if object_type in type_names_key:
        tmp = str(object)
        if tmp == "None" or tmp == "nan" or tmp == "0" or tmp == "" or tmp == "False":
            print(type_names[object_type] + ":", object, object_type)
            return 0
    print("Type not Found")
    return 1