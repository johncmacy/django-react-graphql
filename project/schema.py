import graphene
from core.schema import Query as core_query

class Query(core_query):
    pass

schema = graphene.Schema(query=Query)