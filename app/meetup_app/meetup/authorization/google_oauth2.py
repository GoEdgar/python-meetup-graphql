import aiohttp
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow

from meetup.dao import get_user, create_user
from .jwt_utils import issue_token

router = APIRouter()
flow = Flow.from_client_secrets_file(
    "client_secret.json",
    scopes=[
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email"
        ]
    )
flow.redirect_uri = "http://127.0.0.1/auth/redirect_auth"
authorization_url, _ = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true')


@router.get("/google")
async def authorization():
    return RedirectResponse(authorization_url)


@router.get("/redirect_auth")
async def oauth_callback(code: str):
    session = aiohttp.ClientSession()
    # Gets access token after user agreed
    # to give asked permissions (view profile)
    response = await session.post(
        "https://oauth2.googleapis.com/token",
        params={
            "client_id": flow.client_config["client_id"],
            "client_secret": flow.client_config["client_secret"],
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": "http://127.0.0.1/auth/redirect_auth"
            }
        )
    creds = await response.json()

    # Gets user profile via Google API
    headers = {"Authorization": f"Bearer {creds['access_token']}"}
    response = await session.get(
        "https://www.googleapis.com/userinfo/v2/me",
        headers=headers
        )
    google_profile = await response.json()

    existed_user = get_user(email=google_profile["email"])
    if not existed_user:
        new_user = create_user(name=google_profile["given_name"],
                               email=google_profile["email"])
        existed_user = new_user

    jwt_token = issue_token(existed_user.id)

    return {"access_token": jwt_token, "token_type": "bearer"}
