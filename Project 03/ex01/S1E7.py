from S1E9 import Character


class Baratheon(Character):

    '''Representing the Baratheon family'''

    def __init__(self, name: str, state: bool = True):

        '''
        Function to init stark class
        '''

        self.first_name = name
        if state is not None:
            self.is_alive = state
        self._Family_Name = "Baratheon"
        self._Eyes = "brown"
        self._Hairs = "dark"


    def __str__(self):
        return f"Vector: ('{self._Family_Name}', '{self._Eyes}', '{self._Hairs}')"

    def __repr__(self):
        return f"Vector: ('{self._Family_Name}', '{self._Eyes}', '{self._Hairs}')"

    @property
    def die(self):

        '''
        Function of Stark class, set is_alive to False
        '''

        self.is_alive = False


class Lannister(Character):

    '''Representing the Lannister family'''

    def __init__(self, name: str, state: bool = True):

        '''
        Function to init stark class
        '''

        self.first_name = name
        if state is not None:
            self.is_alive = state
        self._Family_Name = "Lannister"
        self._Eyes = "blue"
        self._Hairs = "light"

    def __str__(self):
        return f"Vector: ('{self._Family_Name}', '{self._Eyes}', '{self._Hairs}')"

    def __repr__(self):
        return f"Vector: ('{self._Family_Name}', '{self._Eyes}', '{self._Hairs}')"


    @property
    def die(self):

        '''
        Function of Stark class, set is_alive to False
        '''

        self.is_alive = False

    def create_lannister():
        print("Hello")
