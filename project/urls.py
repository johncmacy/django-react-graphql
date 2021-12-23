from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', include('users.urls')),
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('api/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
