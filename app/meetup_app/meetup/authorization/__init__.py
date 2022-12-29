from fastapi import APIRouter

from .google_oauth2 import router as google_oauth2_authentication
from .password_auth import router as password_authentication
from .password_register import router as password_registration

auth_router = APIRouter(prefix="/auth")
auth_router.include_router(google_oauth2_authentication)
auth_router.include_router(password_authentication)
auth_router.include_router(password_registration)
