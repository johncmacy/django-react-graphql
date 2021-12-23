import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime(required=False)

class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(username='John', last_login=datetime.now()),
            User(username='Abigail', last_login=datetime.now()),
        ][:first]

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, username):
        if info.context.get('is_vip'):
            username = str(username).upper()
        user = User(username=username)
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

result = schema.execute(
    '''
    mutation createUser($username: String) {
        createUser(username: $username) {
            user {
                username
            }
        }
    }
    ''',
    variable_values = {'username': 'Davey'},
    context={'is_vip': True}
)

print(json.dumps(dict(result.data.items()), indent=4))