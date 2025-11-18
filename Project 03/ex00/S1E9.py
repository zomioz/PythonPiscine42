from abc import ABC, abstractmethod

class Character(ABC):

    '''
    Abstract class Character
    Need 2 asbstract method: is_alive & die
    '''

    @abstractmethod
    def is_alive(self):
        pass
    def die(self):
        pass


class Stark(Character):

    '''
    Class that inherit from Character
    Argument: a name, and a bool state by default on True
    '''

    def __init__(self, name: str, state: bool = True):

        '''
        Function to init stark class
        '''

        self._Name = name
        if state is not None:
            self._State = state

    @property
    def is_alive(self):

        '''
        Function of Stark class, print Self_State
        '''

        print(self._State)

    def die(self):

        '''
        Function of Stark class, set State to False
        '''

        self._State = False
