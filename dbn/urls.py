from django.urls import path
from . import views

app_name = 'dbn'
urlpatterns = [
    path('', views.DbnsView.as_view(), name='dbn'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]