from fastapi import APIRouter, Depends

from meetup.authorization.auth_middleware import get_current_user
from meetup.dao import get_all_meetups
from meetup.model import UserModel
from utils import model_to_dict

router = APIRouter(prefix="/meetup")


@router.get("/")
async def list_meetups(_: UserModel = Depends(get_current_user)):
    meetups = get_all_meetups()
    return [model_to_dict(obj) for obj in meetups]


@router.post("/")
async def create_meetup(_: UserModel = Depends(get_current_user)):
    pass


@router.patch("/meetup/{meetup_id}")
async def update_meetup(meetup_id, _: UserModel = Depends(get_current_user)):
    pass


@router.put("/meetup/{meetup_id}")
async def replace_meetup(meetup_id, _: UserModel = Depends(get_current_user)):
    pass
