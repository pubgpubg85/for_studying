from django.urls import path
from . import views

app_name = 'proportion'
urlpatterns = [
    path('', views.proportion, name='proportion'),
]
