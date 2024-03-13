from django.urls import path
from . import views
from .views import RegisterView

app_name = 'main_page'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('registrate', RegisterView.as_view(), name='registrate'),
]
