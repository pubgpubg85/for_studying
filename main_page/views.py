from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
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
