from django.db import models


# Create your models here.
# 测试题模型
class Question(models.Model):
    q_title = models.CharField(max_length=200)  # 测试题考题
    q_scope = models.CharField(max_length=50)  # 测试题范围
    q_type = models.CharField(max_length=20)  # 测试题类型
    q_content = models.CharField(max_length=500)  # 测试题内容
    q_options = models.CharField(max_length=500)  # 测试题选项，用|作为分隔符。
    q_standard_answer = models.CharField(max_length=500)  # 测试题标准答案。如果是选择题用|作为分隔符。


# 试卷模板
class ExamTemplate(models.Model):
    template_name = models.CharField(max_length=200)  # 试卷模板名称
    question_id_list = models.CharField(max_length=2000)  # 考题id集合
    creator = models.CharField(max_length=50)  # 试卷创建人
    create_time = models.DateTimeField(auto_now=True)  # 试卷创建时间


# 试卷信息
class Exam(models.Model):
    exam_template_id = models.IntegerField(default=1)  # 试卷模板id
    exam_name = models.CharField(max_length=100)  # 试卷名称
    creator = models.CharField(max_length=50)  # 试卷创建人
    create_time = models.DateTimeField(auto_now=True)  # 试卷创建时间
    answer_user_name = models.CharField(max_length=50)  # 答题人姓名


# 答题人给出的答案
class Answer(models.Model):
    exam_id = models.IntegerField()  # 试卷编号
    q_id = models.IntegerField()  # 考题ID
    q_answer = models.CharField(max_length=500)  # 答题人给出的答案。如果是选择题用|作为分隔符。
    score = models.IntegerField()  # 得分
    create_time = models.DateTimeField(auto_now=True)  # 答题时间
