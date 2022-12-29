from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from meetup.dao import get_user
from .exceptions import CredentialCommonException
from .jwt_utils import get_user_id_from_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user_id = get_user_id_from_token(token)

    user = get_user(id=user_id)
    if user is None:
        raise CredentialCommonException

    return user
