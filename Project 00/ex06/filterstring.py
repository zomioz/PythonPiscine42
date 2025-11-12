import sys
from ft_filter import ft_filter


def checker_arg():

  '''
  function to check argument of the program
  no argument
  return 1 on Fail, 0 on succes
  '''

  number_of_arg = len(sys.argv) - 1

  try:
      if number_of_arg != 2:
          raise AssertionError("the arguments are bad")
      try:
          number = int(sys.argv[2])
      except ValueError:
          raise AssertionError("the arguments are bad")
  except AssertionError as Error:
      print("AssertionError:", Error)
      return 1
  return 0


def main():

    '''
    main of the program, launch checker and printf ft_filter output
    no arguments
    no return
    '''

    if checker_arg() == 1:
        exit()

    tmp = sys.argv[1]
    number = int(sys.argv[2])
    words = string.split()

    result = ft_filter(lambda word: len(word) > number, words)

    print(result)


if __name__ == "__main__":
    main()
