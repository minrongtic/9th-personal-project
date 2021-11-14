from django.shortcuts import render
from allauth.account.views import PasswordChangeView
from django.urls import reverse
# Create your views here.


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("route:main")
