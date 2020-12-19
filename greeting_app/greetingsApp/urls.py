from django.contrib import admin
from django.urls import path
from greetingsApp import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path(r'swagger-doc/', schema_view),
    path('', views.index, name='index'),
    path('show',views.show, name='show'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
