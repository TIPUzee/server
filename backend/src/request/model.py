from typing import Type, Callable, Any
from ..users import *
from .response import Response
from .input import Input

class Request: 
    Response = Response
    Input = Input

    __handler_count = 0

    @staticmethod
    def token():
        def decorator(func: Callable[[dict[str, Any]], Any]) -> Callable:
            def wrapper():
                print('token wrapper')
                'check if the user is valid'
                token: dict = {'user_type': 'Admin'}
                func(token)
            wrapper.__name__ = func.__name__ + '_handler_func'
            return wrapper

        decorator.__name__ = decorator.__name__ + \
            '_handler_dec_' + str(Request.__handler_count)
        Request.__handler_count += 1
        return decorator

    @staticmethod
    def authenticate():
        def decorator(func: Callable[[Person], None]):
            def wrapper(token: dict[str, Any]):
                'check if the user is valid'
                print('authenticate wrapper')
                kwargs = {}
                return func(Admin())
            wrapper.__name__ = func.__name__ + '_handler_func'
            return wrapper

        decorator.__name__ = decorator.__name__ + \
            '_handler_dec_' + str(Request.__handler_count)
        Request.__handler_count += 1
        return decorator

    @staticmethod
    def authorize(users: list[Type[Person]]):
        def decorator(func: Callable[[dict[str, Any]], Any]):
            def wrapper(token: dict[str, Any]):
                user_type = eval(token['user_type'])
                if not users: 
                    return func(token)
                elif any([issubclass(user_type, _user) for _user in users]):
                    return func(token)
                else:
                    raise Response.unauthorized()
            wrapper.__name__ = func.__name__ + '_handler_func'
            return wrapper

        decorator.__name__ = decorator.__name__ + \
            '_handler_dec_' + str(Request.__handler_count)
        Request.__handler_count += 1
        return decorator
