import aiohttp
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow

router = APIRouter(prefix="/auth")
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
    async with aiohttp.ClientSession() as session:
        async with session.post(
                "https://oauth2.googleapis.com/token",
                params={
                    "client_id": flow.client_config["client_id"],
                    "client_secret": flow.client_config["client_secret"],
                    "code": code,
                    "grant_type": "authorization_code",
                    "redirect_uri": "http://127.0.0.1/auth/redirect_auth"
                    }
                ) as r:
            creds = await r.json()

        headers = {"Authorization": f"Bearer {creds['access_token']}"}
        async with session.get("https://www.googleapis.com/userinfo/v2/me", headers=headers) as r:
            return await r.json()
