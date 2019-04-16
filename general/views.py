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
                'index': 'customerlist',
                'name': '客户列表',
                'path': '/customerlist'
            }, {
                'index': 'config',
                'name': '配置管理',
                'path': '/config'
            }]}
    return HttpResponse(json.dumps(data),
                        content_type="application/json")
