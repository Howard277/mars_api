from django.urls import path
from .views import *
from .views_user import *

urlpatterns = [
    path('login', login),
    path('getUserPage', get_user_page)
]
