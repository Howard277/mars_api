from django.shortcuts import render
from .models import User
from django.core import serializers
import json
from django.http import HttpResponse, HttpRequest


# Create your views here.
def login(request):
    login_name = request.POST['loginname']
    password = request.POST['password']
    if (login_name is not None) and (password is not None):
        user_list = User.objects.filter(login_name=login_name, password=password)
        if user_list.count() > 0:
            user = user_list[0]  # type:User
            return HttpResponse(json.loads('true'),
                                content_type="application/json")
    return HttpResponse(json.loads('false'),
                        content_type="application/json")
