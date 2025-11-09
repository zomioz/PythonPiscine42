import sys


def checker_arg() -> int:

    '''
    Checker of Arguments, count and check the number of arguments.
    Protected by a try/except to avoid any crash.
    Return 1 or 0, so thee main can exit()
    '''

    number_of_arg = len(sys.argv) - 1

    try:
        if number_of_arg > 1:
            raise AssertionError("Too many Argument")
        elif number_of_arg <= 0:
            raise AssertionError("Please provide a string to the program")
        elif len(sys.argv[1]) < 1:
            raise AssertionError("Argument length must be > 1")
        else:
            return 0
    except AssertionError as error:
        print("AssertionError :", error)
        return 1


def count_everything() -> dict:

    '''
    Function to count every char of the program input protectd by a try/except.
    Count everything with the sum() function, store it in the database dict.
    return the dict or NULL if an error occurs.
    '''

    database = {
        "characters": 0,
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digit": 0
    }
    tmp = sys.argv[1]
    all_punctuation = "!\"$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    try:
        database["characters"] = len(tmp)
        database["upper"] = sum(1 for c in tmp if c.isupper())
        database["punctuation"] = sum(1 for c in tmp if c in all_punctuation)
        database["lower"] = sum(1 for c in tmp if c.islower())
        database["spaces"] = sum(1 for c in tmp if c.isspace())
        database["digit"] = sum(1 for c in tmp if c.isdigit())

    except AssertionError:
        print("AssertionError : Error during counting")
        return 0

    return database


def print_everything(database: dict):

    '''
    Simple function to write every data in database dict.
    Arg: dict database that store int from count_everything().
    No return
    '''

    print("The text contains", database["characters"], "characters:")
    print(database["upper"], "upper letters")
    print(database["lower"], "lower letters")
    print(database["punctuation"], "punctuation marks")
    print(database["spaces"], "spaces")
    print(database["digit"], "digits")


def main():

    '''
    Main of the program, launch every function.
    Exit() if a function fail.
    '''

    if checker_arg() == 1:
        exit()
    database = count_everything()
    if database == 0:
        exit()
    print_everything(database)


if __name__ == "__main__":
    main()
