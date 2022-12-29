from fastapi import APIRouter
from passlib.context import CryptContext

from meetup.dao import get_user, create_user
from .dataclasses import Token, RegisterBody
from .jwt_utils import issue_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register", response_model=Token)
async def register_new_user(login_data: RegisterBody):
    existed_user = get_user(email=login_data.email)
    if existed_user:
        raise CredentialConflictException

    new_user = create_user(email=login_data.email,
                           password_hash=pwd_context.hash(login_data.password))
    access_token = issue_token(new_user.id)

    return {"access_token": access_token, "token_type": "bearer"}
