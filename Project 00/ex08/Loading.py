import os


def check_terminal_size(terminal: tuple, lst:range) -> list:

    '''
    Function to check the size of progression bar and end of progression bar in function of the terminal size
    Argument: a tuple that correspond to the return of os.get_terminal_size(), and the range of the function range()
    Return: a list that contain in [0] the progression_bar size, and in [1] the end size
    '''

    terminal_size = int(terminal[0])
    range_size = len(str(len(lst)))
    start_size = 5
    end_size = 28 + (range_size * 2)

    if terminal_size >= start_size + end_size + 1:
        return [terminal_size - (start_size + end_size), end_size]
    else:
        return [1, terminal_size - 5 - 1]


def print_everything(length: int, x: int, number_of_chr: int, size: int) -> None:

    '''
    Display the progression bar
    Argument: first length of range, second iterator x, third number of char max, fourth size of progression bar 
    Return: None
    '''

    print(int((x * 100 / length)), end ="")
    print("%|", end="")
    print("█" * number_of_chr, end="")
    if number_of_chr < size:
        print(" " * (size - number_of_chr), end="")
    print("|", length, end="")
    print("/", end="")
    print(length, end="\r")


def ft_tqdm(lst: range) -> None:

    '''
    Function ft_tqdm, replicate the original function tqdm
    Argument: a range
    Return: None
    '''

    try :
        terminal_size_tuple = os.get_terminal_size()
        size_progression_bar = check_terminal_size(terminal_size_tuple, lst)

        x = 0
        length = len(lst)
        size = size_progression_bar[0]

        while x <= length:
            number_of_chr = int(size * float(x * 100 / len(lst)) / 100)
            print_everything(length, x, number_of_chr, size)
            x += 1
            yield x

    except OSError:
        print("OSError : fd from get_terminal_size isn't link to a terminal")
