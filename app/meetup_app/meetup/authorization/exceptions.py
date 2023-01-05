from fastapi import HTTPException
from starlette import status

CredentialCommonException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
    )

CredentialNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found",
    headers={"WWW-Authenticate": "Bearer"},
    )

CredentialInvalidPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect password",
    headers={"WWW-Authenticate": "Bearer"},
    )

CredentialConflictException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User with that email already exists",
    )
