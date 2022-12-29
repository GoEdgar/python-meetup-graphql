from datetime import datetime, timedelta

from jose import jwt, JWTError

from .exceptions import CredentialCommonException

SECRET_KEY = "0425450f9bf5d74091813ef7d8ec7cc7"


def get_user_id_from_token(token):
    try:
        print(token, type(token))
        token_data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except JWTError as e:
        print(e)
        raise CredentialCommonException

    user_id = token_data.get("sub")
    if user_id is None:
        print("user id is empty")
        raise CredentialCommonException

    return user_id


def issue_token(user_id: int):
    data = {"sub": str(user_id)}
    expire = datetime.utcnow() + timedelta(minutes=15)
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm="HS256")
    return encoded_jwt
