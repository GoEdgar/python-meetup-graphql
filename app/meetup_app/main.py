from fastapi import FastAPI
from meetup.graphql_api import graphql_app
from meetup.rest_api import rest_router

app = FastAPI()
app.include_router(rest_router)
app.mount("/graphql", graphql_app)
