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
        return query.filter(UserModel.id == id)
    return query


def get_user(*, id=None, email=None):
    query = session.query(UserModel)
    if id:
        return query.filter(UserModel.id == id).one_or_none()
    if email:
        return query.filter(UserModel.email == email).one_or_none()

    raise ValueError


def create_user(**kwargs):
    new_user = UserModel(**kwargs)
    session.add(new_user)
    session.commit()
    return new_user
