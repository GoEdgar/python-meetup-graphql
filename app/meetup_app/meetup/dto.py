from meetup.model import Session, UserModel, MeetupModel

session = Session()


def get_all_meetups():
    return session.query(MeetupModel).all()


def get_meetup_query(*, id=None, place=None, keyword=None, contains_in_title=None):
    query = session.query(MeetupModel)
    if id:
        return query.filter(MeetupModel.id == id)
    if place:
        query = query.filter(MeetupModel.place == place)
    if keyword:
        query = query.filter(MeetupModel.keywords.contains({keyword}))
    if contains_in_title:
        query = query.filter(MeetupModel.title.contains(contains_in_title))
    return query


def get_user_query(*, id=None):
    query = session.query(UserModel)
    if id:
        return query.filter(MeetupModel.id == id)
    return query
