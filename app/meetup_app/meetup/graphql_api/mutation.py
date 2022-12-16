import graphene
from graphene import String, Field, List, DateTime, Int

from meetup.model import Session
from .query import User, Meetup

session = Session()

class CreateUser(graphene.Mutation):
    class Arguments:
        name = String()
        username = String()
        email = String()

    user = Field(User)

    async def mutate(*_, **kwargs):
        new_user = User(**kwargs)
        session.add(new_user)
        session.commit()
        return new_user


class CreateMeetup(graphene.Mutation):
    class Arguments:
        title = String()
        description = String()
        keywords = List(String)
        place = String()
        date = DateTime()
        created_by = Int()

    meetup = Field(Meetup)

    async def mutate(*_, **kwargs):
        new_meetup = Meetup(**kwargs)
        session.add(new_meetup)
        session.commit()
        return new_meetup


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
