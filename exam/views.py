from .models import *
import json
from django.http import HttpResponse
from mars_api.tools import model_to_dict, queryset_to_dict, save_model
from django.db.models import Q


# Create your views here.
# 保存考题
def save_question(request):
    question = save_model(request, Question)
    return HttpResponse(json.dumps(model_to_dict(question)),
                        content_type="application/json")


# 通过考题id获取考题
def get_question_by_id(request):
    id = request.GET.get('id', -1)  # 获取请求参数id ，默认值为-1
    questions = Question.objects.filter(id=id)
    question = Question()
    if len(questions) > 0:
        question = questions[0]
    return HttpResponse(json.dumps(model_to_dict(question)),
                        content_type="application/json")


# 通过查询条件获取考题
def get_question_by_condition(request):
    params = json.loads(request.body.decode(encoding='utf-8'))
    page_index = params.get('pageIndex', 0)  # 获取页索引
    page_size = params.get('pageSize', 0)  # 获取页尺寸
    condition = params.get('condition', '')
    q_list = Question.objects.all()
    if len(condition) > 0:
        q_list = q_list.filter(Q(title__contains=condition) | Q(scope=condition))
    count = q_list.count()
    q_list = q_list[page_index * page_size, (page_index + 1) * page_size]
    data = {'pageIndex': page_index, 'pageSize': page_size, 'count': count, 'data': queryset_to_dict(q_list)}
    return HttpResponse(json.dumps(data),
                        content_type="application/json")


# 保存试卷模板
def save_exam_template(request):
    exam_template = save_model(request, ExamTemplate)
    return HttpResponse(json.dumps(model_to_dict(exam_template)),
                        content_type="application/json")


# 通过试卷模板id获取试卷
def get_exam_template_by_id(request):
    id = request.GET.get('id', -1)  # 获取请求参数id ，默认值为-1
    exam_template = ExamTemplate()
    exam_template_s = ExamTemplate.objects.filter(id=id)
    if exam_template_s.count > 0:
        exam_template = exam_template_s[0]
    return HttpResponse(json.dumps(model_to_dict(exam_template)),
                        content_type="application/json")


# 通过查询条件获取试卷模板
def get_exam_template_condition(request):
    params = json.loads(request.body.decode(encoding='utf-8'))
    page_index = params.get('pageIndex', 0)  # 获取页索引
    page_size = params.get('pageSize', 0)  # 获取页尺寸
    condition = params.get('condition', '')
    et_list = ExamTemplate.objects.all()
    if len(condition) > 0:
        et_list = et_list.filter(template_name__contains=condition)
    count = et_list.count()
    et_list = et_list[page_index * page_size, (page_index + 1) * page_size]
    data = {'pageIndex': page_index, 'pageSize': page_size, 'count': count, 'data': queryset_to_dict(et_list)}
    return HttpResponse(json.dumps(data),
                        content_type="application/json")


# 保存试卷
def save_exam(request):
    exam = save_model(request, Exam)
    return HttpResponse(json.dumps(model_to_dict(exam)),
                        content_type="application/json")


# 通过考卷id获得考卷
def get_exam_by_id(request):
    id = request.GET.get('id', -1)  # 获取请求参数id ，默认值为-1
    exam = Exam()
    exam_s = Exam.objects.filter(id=id)
    if exam_s.count > 0:
        exam = exam_s[0]
    return HttpResponse(json.dumps(model_to_dict(exam)),
                        content_type="application/json")


# 通过查询条件获取试卷
def get_exam_condition(request):
    params = json.loads(request.body.decode(encoding='utf-8'))
    page_index = params.get('pageIndex', 0)  # 获取页索引
    page_size = params.get('pageSize', 0)  # 获取页尺寸
    condition = params.get('condition', '')
    e_list = Exam.objects.all()
    if len(condition) > 0:
        e_list = e_list.filter(
            Q(exam_name__contains=condition) | Q(exam_template_id=condition) | Q(answer_user_name=condition))
    count = e_list.count()
    e_list = e_list[page_index * page_size, (page_index + 1) * page_size]
    data = {'pageIndex': page_index, 'pageSize': page_size, 'count': count, 'data': queryset_to_dict(e_list)}
    return HttpResponse(json.dumps(data),
                        content_type="application/json")


def save_answer(request):
    answer = save_model(request, Answer)
    return HttpResponse(json.dumps(model_to_dict(answer)),
                        content_type="application/json")
