from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', include('users.urls')),
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),

    # REST:
    path('api/', include('api.urls')),

    # GraphQL:
    path('gql/', GraphQLView.as_view(schema=schema, graphiql=True)),
]
