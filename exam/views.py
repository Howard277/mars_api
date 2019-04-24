from .models import *
import json
from django.http import HttpResponse
from mars_api.tools import model_to_dict


# Create your views here.
# 保存考题
def save_question(request):
    question = Question()  # type:Question
    body = json.loads(request.body.decode(encoding='utf-8'))
    id = body.get('id')
    if id is not None and len(id) > 0:
        # 有id表示更新，从数据库中读取数据
        question = Question.objects.get(id=id)

    question.q_title = body.get('title')
    question.q_scope = body.get('scope')
    question.q_type = body.get('type')
    question.q_content = body.get('content')
    question.q_options = body.get('options')
    question.q_standard_answer = body.get('standard_answer')
    question.save()
    return HttpResponse(json.dumps(model_to_dict(question)),
                        content_type="application/json")


# 通过问题id获取考题
def get_question_by_id(request):
    id = request.GET.get('id', -1)  # 获取请求参数id ，默认值为-1
    questions = Question.objects.filter(id=id)
    if len(questions) > 0:
        return questions[0]
    else:
        return None
