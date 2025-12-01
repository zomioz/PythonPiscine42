class calculator:
    '''A Class that can make calculs'''

    def __init__(self, object):
        '''Init calculator class, take a vector as argument'''
        self.vector = object

    def __add__(self, object) -> None:
        '''function to add a scalar to the vector, one scalar argument'''
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        '''function to multiply a scalar to the vector, one scalar argument'''
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        '''function to substract a scalar to the vector, one scalar argument'''
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        '''function to divid a scalar to the vector, one scalar argument'''
        if not object:
            return print("Error: Can't divide by 0")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
