from typing import Callable

from ...users import Person
from ..response import Response
from flask import request

class Input: 
    __handler_count = 0

    @staticmethod
    def Json(**fields): 
        def decorator(func: Callable[..., None]):
            def wrapper(user: Person, *args, **kwargs):
                try:
                    json: dict = request.get_json()
                except: 
                    raise Response.bad(reason='NOT a JSON request.')
                for key in fields.keys(): 
                    if fields[key] and key not in json: 
                        raise Response.field_not_found(key)
                return func(user, *args, **json, **kwargs)

            wrapper.__name__ = func.__name__ + '_handler_func'
            return wrapper

        decorator.__name__ = decorator.__name__ + \
            '_handler_dec_' + str(Input.__handler_count)
        Input.__handler_count += 1
        return decorator


    @staticmethod
    def Url(**fields): 
        def decorator(func: Callable[..., None]):
            def wrapper(user: Person, *args, **kwargs):
                try:
                    json: dict = request.args
                except: 
                    raise Response.bad(reason='NOT a JSON request.')
                for key in fields.keys(): 
                    if fields[key] and key not in json: 
                        raise Response.field_not_found(key)
                return func(user, *args, **json, **kwargs)

            wrapper.__name__ = func.__name__ + '_handler_func'
            return wrapper

        decorator.__name__ = decorator.__name__ + \
            '_handler_dec_' + str(Input.__handler_count)
        Input.__handler_count += 1
        return decorator
