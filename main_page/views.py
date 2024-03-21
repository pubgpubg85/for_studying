from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from main_page.forms import RegisterForm


@login_required
def main_page(request):
    return render(request, 'main_page/index.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('main_page:main_page')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        User.objects.create_user(username=username, email=email, password=password)
        return super().form_valid(form)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # Check if "remember me" checkbox is checked

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            if remember_me:
                # Set session expiration time to a longer period
                request.session.set_expiry(settings.REMEMBER_ME_SESSION_EXPIRY)
            else:
                # Use the default session expiration time
                request.session.set_expiry(0)  # Session expires when the user closes the browser

            return redirect('main_page:main_page')  # Redirect to the main page after login

    return render(request, 'registration/login.html')
