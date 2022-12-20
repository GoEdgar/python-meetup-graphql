from fastapi import FastAPI

from meetup.authorization import auth_router
from meetup.rest_api import rest_router
from meetup.graphql_api import graphql_app

app = FastAPI()
app.include_router(auth_router)
app.include_router(rest_router)
app.mount("/graphql", graphql_app)
