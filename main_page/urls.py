from django.urls import path
from . import views

app_name = 'main_page'
url_patterns = [
    path('', views.main_page, name='main_page'),
]
