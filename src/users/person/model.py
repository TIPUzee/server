from typing import Type, final
from abc import ABC


class Person(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._id: int = -1
        self._name: str = ''
        self._age: int = -1

    @final
    @property
    def id(self): 
        return self._id

    @final
    @id.setter
    def id(self, value): 
        self._id = value

    @final
    @property
    def name(self): 
        return self._name

    @final
    @name.setter
    def name(self, value): 
        self._name = value

    @final
    @property
    def age(self): 
        return self._age

    @final
    @age.setter
    def age(self, value): 
        self._age = value

    def __str__(self) -> str:
        res = f'\n{self.__class__}'
        for key in dir(self):
            if not key.startswith('_'):
                val = getattr(self, key)
                if type(val) == str: 
                    res += f'\n\t{key}:{type(val)}="{val}"  '
                else:
                    res += f'\n\t{key}:{type(val)}={val}  '
        return res
