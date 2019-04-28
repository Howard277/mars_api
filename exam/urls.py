from django.urls import path
from .views import *

urlpatterns = [
    path('getQuestionById', get_question_by_id),
    path('saveQuestion', save_question),
    path('getQuestionByCondition', get_question_by_condition),
    path('saveExamTemplate', save_exam_template),
    path('getExamTemplateById', get_exam_template_by_id),
    path('getExamTemplateCondition', get_exam_template_condition),
    path('saveExam', save_exam),
    path('getExamById', get_exam_by_id),
    path('saveAnswer', save_answer),
    path('getAnswerCondition', get_answer_condition)
]
