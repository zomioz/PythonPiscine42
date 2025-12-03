def ft_statistics(*args: any, **kwargs: any) -> None:

    '''
    Function that calcul mathematical expression
    Argument : multiple store in args and kwargs
    Return: None
    '''

    if not kwargs:
        return print("ERROR : No mathematical operation asked")
    if not args:
        for x in kwargs:
            print("ERROR")
        return

    for x in kwargs:
        match kwargs[x]:
            case "mean":

                total = 0
                for x in args:
                    total += x
                total = total / len(args)
                print("mean :", total)

            case "median":

                arg = list(args)
                arg.sort()
                num = len(arg)//2

                if len(arg) % 2 != 0:
                    print("median :", arg[num])
                elif len(arg) % 2 == 0:
                    print("median :", (arg[num - 1] + arg[num]) / 2)

            case "quartile":

                arg = list(args)
                arg.sort()
                num = len(arg)//4

                if len(arg) % 2 != 0:
                    print("quartile :", [arg[num], arg[num * 3]])
                elif len(arg) % 2 == 0:
                    print("quartile :",
                          [(arg[num * 3 - 1] + arg[num * 3]) / 2,
                           (arg[num * 3 - 1] + arg[num * 3]) / 2])

            case "std":

                average = 0
                for x in args:
                    average += x
                average = average / len(args)

                std = 0
                for x in args:
                    std += (x - average) ** 2
                std = std / len(args)
                print("std :", std ** 0.5)

            case "var":

                average = 0
                for x in args:
                    average += x
                average = average / len(args)

                std = 0
                for x in args:
                    std += (x - average) ** 2
                std = std / len(args)
                print("var :", std)
