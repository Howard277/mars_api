from .models import User
from django.http import HttpResponse
import json
from mars_api.tools import queryset_to_dict


# 获取分页用户信息
def get_user_page(request):
    pageIndex = request.POST['pageIndex'] if ('pageIndex' in request.POST) and request.POST['pageIndex'] else 0
    pageSize = request.POST['pageSize'] if ('pageSize' in request.POST) and request.POST['pageSize'] else 10
    all = User.objects.all()
    count = all.count()
    userList = all[pageIndex * pageSize:(pageIndex + 1) * pageSize]
    data = {"count": count, "userList": queryset_to_dict(userList)}
    return HttpResponse(json.dumps(data),
                        content_type="application/json")
