from .app import APP
from src.request import Request
from src.users import Admin, Person, User
from src.utils.enums import *


@APP.route('')
@Request.Response.handle()
def home(**kwargs: dict) -> None:
    raise Request.Response.success(test='Hii')

@APP.route('/test')
@Request.Response.handle()
@Request.token()
@Request.authorize(users=[Admin])
@Request.authenticate()
@Request.Input.Url(fname=OPTIONAL)
@Request.Input.Json(name=REQUIRED)
def test(user: Admin, **kwargs: dict) -> None:
    print(user)
    raise Request.Response.success(test='Hii')
