from datetime import datetime
import traceback
from typing import Callable


class Response(Exception):
    def __init__(self, response_code:int, _html:str='', **kwargs) -> None:
        self.response_code = response_code
        self.kwargs = kwargs
        self._html: str = _html

    def res(self):
        if self._html: 
            return self._html, self.response_code
        return self.kwargs, self.response_code

    __handler_count = 0

    @staticmethod
    def html(_html:str):
        return Response(response_code=200, _html=_html)

    @staticmethod
    def success(**kwargs):
        return Response(response_code=200, status='Success', **kwargs)

    @staticmethod
    def unauthenticated(**kwargs):
        return Response(response_code=401, status='Unauthenticated', **kwargs)

    @staticmethod
    def unauthorized(**kwargs):
        return Response(response_code=401, status='Unauthorized', **kwargs)

    @staticmethod
    def bad(**kwargs):
        return Response(response_code=400, status='Bad', **kwargs)

    @staticmethod
    def field_not_found(field: str, **kwargs):
        return Response(response_code=400, status='Field NOT Found', field=field, **kwargs)

    @staticmethod
    def server(**kwargs):
        return Response(response_code=500, status='Internal Server Error', **kwargs)

    @staticmethod
    def handle():
        def decorator(func: Callable[[], None]):
            def wrapper():
                try:
                    func()
                    raise Response.server(reason='NO Request Response Was Raised')
                except Response as e:
                    return e.res()

                except Exception as e:
                    return {'msg': 'Internal server error [Unhandled Exception]', 'exception': traceback.format_exception(e), 'dialog': 101}, 500

                except BaseException as e:
                    return {'msg': 'Internal server error [Unhandled BaseException]', 'exception': traceback.format_exception(e), 'dialog': 101}, 500

            wrapper.__name__ = func.__name__ + '_handler_func'
            return wrapper

        decorator.__name__ = decorator.__name__ + \
            '_handler_dec_' + str(Response.__handler_count)
        Response.__handler_count += 1
        return decorator

