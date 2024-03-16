from django.urls import path
from . import views
from .views import RegisterView
from django.contrib.auth import views as auth_views

app_name = 'main_page'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('registrate', RegisterView.as_view(), name='registrate'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="pwd_reset/reset_password.html"),
         name="reset_password"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="pwd_reset/password_reset_form.html"),
         name="password_reset_confirm"),

    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="pwd_reset/reset_sent.html"),
         name="password_reset_done"),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="pwd_reset/password_reset_done.html"),
         name="password_reset_complete"),
    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password/reset_password.html"),
    #      name='reset_password'),
    # path('reset_password_sent/',
    #      auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
