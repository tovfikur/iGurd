from .models import UserToken
from .models import UserDetails


def check_token(token):
    token_obj = UserToken.objects.filter(token=token)
    try:
        if token_obj[0]:
            return (True,token_obj[0].user)
    except Exception :
        return (False,'')