from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

from meetup.dao import get_user
from .dataclasses import Token
from .exceptions import CredentialNotFoundException
from .jwt_utils import issue_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    existed_user = get_user(email=form_data.username)
    if not existed_user:
        raise CredentialNotFoundException
    is_authenticated = pwd_context.verify(form_data.password, existed_user.password_hash)
    if not is_authenticated:
        raise CredentialInvalidPasswordException

    access_token = issue_token(existed_user.id)
    return {"access_token": access_token, "token_type": "bearer"}
