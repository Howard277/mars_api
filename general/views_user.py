from .models import User
from django.http import HttpResponse, QueryDict
import json
from mars_api.tools import queryset_to_dict


# 获取分页用户信息
def get_user_page(request):
    post = request.POST  # type:QueryDict
    pageIndex = post.get('pageIndex', 0)
    pageSize = post.get('pageSize', 10)
    all = User.objects.all()
    count = all.count()
    userList = all[pageIndex * pageSize:(pageIndex + 1) * pageSize]
    data = {"count": count, "userList": queryset_to_dict(userList)}
    return HttpResponse(json.dumps(data),
                        content_type="application/json")
