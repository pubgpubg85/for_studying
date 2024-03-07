from django.urls import path
from . import views

app_name = 'interpolation'
urlpatterns = [
    path('', views.interpolation, name='interpolation'),
]
