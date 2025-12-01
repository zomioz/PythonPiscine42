from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    '''Representing the King'''

    def __init__(self, name: str):
        '''
        Function to init Baratheon and Lannister class
        '''

        Lannister.__init__(self, name)
        Baratheon.__init__(self, name)

    def set_family_name(self, name: str):
        '''set family_name, take one str argument'''
        self.family_name = name

    def set_eyes(self, color: str):
        '''set eyes, take one str argument'''
        self.eyes = color

    def set_hairs(self, color: str):
        '''set hairs, take one str argument'''
        self.hairs = color

    def get_family_name(self):
        '''Return family_name'''
        return self.family_name

    def get_eyes(self):
        '''Return eyes'''
        return self.eyes

    def get_hairs(self):
        '''Return hairs'''
        return self.hairs
