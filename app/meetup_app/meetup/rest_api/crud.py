from fastapi import APIRouter

from meetup import dto
from utils import model_to_dict

router = APIRouter(prefix="/meetup")


@router.get("/")
async def get_all_meetups():
    meetups = dto.get_all_meetups()
    return [model_to_dict(obj) for obj in meetups]


@router.post("/")
async def create_meetup():
    pass


@router.patch("/meetup/{meetup_id}")
async def update_meetup(meetup_id):
    pass


@router.put("/meetup/{meetup_id}")
async def replace_meetup(meetup_id):
    pass
