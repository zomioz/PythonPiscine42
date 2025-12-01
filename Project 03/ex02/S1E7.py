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
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

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
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):

        '''
        Function of Stark class, set is_alive to False
        '''

        self.is_alive = False

    @classmethod
    def create_lannister(cls, name: str, state: bool = True):

        '''
        Class method to create a Lannister character
        '''

        return cls(name, state)
