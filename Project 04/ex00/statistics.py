def ft_statistics(*args: any, **kwargs: any) -> None:
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
                arguments = list(args)
                arguments.sort()
                length = len(arguments)//2

                if len(arguments) % 2 != 0:
                    print("median :", arguments[length])
                elif len(arguments) % 2 == 0:
                    print("median :", (arguments[length - 1] + arguments[length]) / 2)

            case "quartile":
                arguments = list(args)
                arguments.sort()
                length = len(arguments)//4

                if len(arguments) % 2 != 0:
                    print("quartile :", [arguments[length], arguments[length * 3]])
                elif len(arguments) % 2 == 0:
                    print("quartile :", [(arguments[length * 3 - 1] + arguments[length * 3]) / 2, (arguments[length * 3 - 1] + arguments[length * 3]) / 2])

            case "std":
                average = 0
                for x in args:
                    average += x
                average = average / len(args)

                std = 0
                for x in args:
                    std += (x - average) * (x - average)
                std = std / len(args)
                print("std :", std)

            case "var":
                print(kwargs[x])
