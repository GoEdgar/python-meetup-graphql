import graphene
from graphene import ID, String, List, DateTime, Field, Argument, Int

from meetup.dao import get_user_query, get_meetup_query
from meetup.model import Session, UserModel

session = Session()


class User(graphene.ObjectType):
    id = ID()
    name = String()
    email = String()


class Meetup(graphene.ObjectType):
    id = ID()
    title = String()
    description = String()
    keywords = List(String)
    place = String()
    date = DateTime()
    created_by = Field(User)

    def resolve_created_by(meetup, _):
        query = session.query(UserModel).filter(UserModel.id == meetup.created_by)
        return query.one()


class Query(graphene.ObjectType):
    users = List(
        User,
        id=Argument(ID, default_value=None)
        )
    meetups = List(
        Meetup,
        id=Argument(ID, default_value=None),
        place=Argument(String, default_value=None),
        keyword=Argument(String, default_value=None),
        contains_in_title=Argument(String, default_value=None)
        )
    meetups_count = Int(
        place=Argument(String, default_value=None),
        keyword=Argument(String, default_value=None)
        )

    def resolve_users(*_, **params):
        query = get_user_query(**params)
        return query.all()

    def resolve_meetups(*_, **params):
        query = get_meetup_query(**params)
        return query.all()

    def resolve_meetups_count(*_, **params):
        query = get_meetup_query(**params)
        return query.count()
