from django.shortcuts import render
from .models import *


# Create your views here.
# 通过问题id获取问题
def get_question_by_id(request):
    id = request.GET.get('id', -1)  # 获取请求参数id ，默认值为-1
    questions = Question.objects.filter(id=id)
    if len(questions) > 0:
        return questions[0]
    else:
        return None
