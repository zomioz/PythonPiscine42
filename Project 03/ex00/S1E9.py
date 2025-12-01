from abc import ABC, abstractmethod


class Character(ABC):

    '''
    Abstract class Character
    Need 2 asbstract method: is_alive & die
    '''

    @abstractmethod
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

        self.first_name = name
        if state is not None:
            self.is_alive = state

    def die(self):

        '''
        Function of Stark class, set State to False
        '''

        self.is_alive = False
