import sys
from ft_filter import ft_filter


def checker_arg():

    '''
    Checker of arg, verify number and type of arg
    no arguments
    return 1 on fail
    '''

    number_of_arg = len(sys.argv) - 1

    try:
        if number_of_arg != 2:
            raise AssertionError("Wrong number of Argument")
        try:
            int(sys.argv[2])
        except ValueError:
            raise AssertionError("Second Argument isn't an integer")

    except AssertionError as Error:
        print("AssertionError :", Error)
        return 1


def main():

    '''
    main of the program, launch checker and ft_filter
    no argument
    no return
    '''

    if checker_arg() == 1:
        exit()

    N = int(sys.argv[2])
    words = sys.argv[1].split()
    result = ft_filter(lambda word: len(word) > N, words)

    print(result)


if __name__ == "__main__":
    main()
