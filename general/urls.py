from django.urls import path
from .views import *
from .views_user import *
from .views_business_system import *

urlpatterns = [
    path('login', login),
    path('getUserPage', get_user_page),
    path('getUser', get_user),
    path('postBusinessSystem', post_business_system),
    path('getBusinessSystemPage', get_business_system_page)
]
