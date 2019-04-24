from django.urls import path
from .views import *

urlpatterns = [
    path('getQuestionById', get_question_by_id),
]
