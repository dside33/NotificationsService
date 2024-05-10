from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm


class RegistrationView(TemplateView):
    template_name = 'login/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomUserCreationForm()
        return context