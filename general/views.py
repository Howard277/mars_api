from .models import User
import json
from django.http import HttpResponse, QueryDict
from mars_api.tools import model_to_dict


# Create your views here.
# 登录接口
def login(request):
    body = request.body  # type:bytes
    params = json.loads(body.decode(encoding='utf-8'))
    login_name = params.get('loginName', '')
    password = params.get('password', '')
    data = {'status': False}
    if (len(login_name) > 0) and (len(password) > 0):
        user_list = User.objects.filter(login_name=login_name, password=password)
        if user_list.count() > 0:
            user = user_list[0]  # type:User
            data = {'status': True, 'userInfo': model_to_dict(user), 'menus': [{
                'index': 'mainpage',
                'name': '首页',
                'path': '/'
            }, {
                'index': 'customermanagement',
                'name': '客户管理'
            }, {
                'index': 'customerList',
                'name': '客户列表',
                'path': '/customerList'
            }, {
                'index': 'authManagement',
                'name': '权限管理'
            }, {
                'index': 'config',
                'name': '配置管理',
                'path': '/config'
            }, {
                'index': 'businessSystemList',
                'name': '业务系统管理',
                'path': '/businessSystemList'
            }, {
                'index': 'businessSystemInfo',
                'name': '业务系统详情',
                'path': '/businessSystemInfo'
            }, {
                'index': 'candidateManagement',
                'name': '候选人管理'
            }, {
                'index': 'candidateList',
                'name': '候选人列表',
                'path': '/candidateList'
            }, {
                'index': 'examManagement',
                'name': '考试管理'
            }, {
                'index': 'questionList',
                'name': '考题列表',
                'path': '/questionList'
            }, {
                'index': 'questionInfo',
                'name': '考题详情',
                'path': '/questionInfo'
            }, {
                'index': 'examTemplateList',
                'name': '试卷模板列表',
                'path': '/examTemplateList'
            }, {
                'index': 'examTemplateInfo',
                'name': '试卷模板详情',
                'path': '/examTemplateInfo'
            }, {
                'index': 'examList',
                'name': '试卷列表',
                'path': '/examList'
            }, {
                'index': 'examInfo',
                'name': '试卷详情',
                'path': '/examInfo'
            }]}
    return HttpResponse(json.dumps(data),
                        content_type="application/json")
