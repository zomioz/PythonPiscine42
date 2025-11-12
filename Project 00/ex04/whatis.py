import sys as sys

try:
    number = len(sys.argv) - 1

    if number >= 2:
        raise AssertionError("Incorrect number of arguments")
    if number < 1:
        exit()

    try:
        number = int(sys.argv[1])
    except:
        raise AssertionError("Argument isn't an integer")

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


except AssertionError as error:
    print("AssertionError:", error)