from .models import User
from django.http import HttpResponse, QueryDict
import json
from mars_api.tools import queryset_to_dict


# 获取分页用户信息
def get_user_page(request):
    post = request.POST  # type:QueryDict
    page_index = post.get('pageIndex', 0)
    page_size = post.get('pageSize', 10)
    all_user = User.objects.all()
    count = all_user.count()
    user_list = all_user[page_index * page_size:(page_index + 1) * page_size]
    data = {"count": count, "userList": queryset_to_dict(user_list)}
    return HttpResponse(json.dumps(data),
                        content_type="application/json")


# 根据条件获取用户数据
def get_user(request):
    get = request.GET  # type:QueryDict
    login_name = get.get('loginName', '')
    real_name = get.get('realName', '')
    user_list = User.objects.all()
    if len(login_name) != 0:
        user_list = user_list.filter(login_name=login_name)
    if len(real_name) != 0:
        user_list = user_list.filter(real_name=real_name)
    return HttpResponse(json.dumps(queryset_to_dict(user_list)), content_type='application/json')
