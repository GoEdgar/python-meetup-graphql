import graphene
from graphene import String, Field, List, DateTime, Int

from meetup.model import Session, UserModel, MeetupModel
from .query import User, Meetup

session = Session()


class CreateUser(graphene.Mutation):
    class Arguments:
        name = String()
        username = String()
        email = String()

    user = Field(User)

    async def mutate(*_, **kwargs):
        new_user = UserModel(**kwargs)
        session.add(new_user)
        session.commit()
        return CreateUser(user=new_user)


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
        new_meetup = MeetupModel(**kwargs)
        session.add(new_meetup)
        session.commit()
        return CreateMeetup(meetup=new_meetup)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_meetup = CreateMeetup.Field()
