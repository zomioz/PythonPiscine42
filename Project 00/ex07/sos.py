import sys


def morse_dictionnary(c: chr) -> str:

    '''
    Function to transform chr in morse code with a dictionnary
    argument: take a chr to convert
    return: str that contain the morse code on succes, and NULL on fail
    '''

    morse_dictionnary = {
        " ": "/",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    if c in morse_dictionnary:
        return morse_dictionnary[c]
    else:
        return 0


def checker_arg() -> bool:
    
    '''
    checker of argument, check the number of argv and if each chr are alphanumeric
    no argument
    return a bool :False on fail, True on succes
    '''

    try:
        number = len(sys.argv) - 1

        if number > 1:
            raise AssertionError("Too many argument")
        if number < 1:
            raise AssertionError("Need more argument")

        tmp = list(sys.argv[1])
        tmp2 = [s.upper() for s in tmp]
        for x in tmp2:
            if morse_dictionnary(x) == 0:
                raise AssertionError("argument must be alphanumeric characters")

        return True

    except AssertionError as Error:
        print("AssertionError :", Error)
        return False


def treat_arg():

    '''
    treat each chr of the argument, and place it in morse_code, then display it
    no Arg
    No return
    '''

    tmp = list(sys.argv[1])
    tmp2 = [s.upper() for s in tmp]
    morse_code = []

    for x in tmp2:
        str = morse_dictionnary(x)
        morse_code.append(str)

    print(" ".join(morse_code))


def main():

    '''
    main function, launch checker and printer of argument
    the program need 1 argument
    '''

    if checker_arg() == False:
        return 1
    
    treat_arg()
    return 0

if __name__ == "__main__":
    main()