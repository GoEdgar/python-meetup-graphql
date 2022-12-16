import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from .mutation import Mutation
from .query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLApp(schema, on_get=make_graphiql_handler())
