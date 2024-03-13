from django.contrib.auth.decorators import login_required
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
        form.save()
        return super().form_valid(form)
