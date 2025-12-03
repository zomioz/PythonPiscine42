import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:

    '''
    Generate a random ID
    No argument
    Return: a str
    '''

    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:

    '''
    Class of a student
    '''

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):

        '''
        Function that's called after init the class
        Argument: self
        No return
        '''

        self.login = self.name[0] + self.surname
