import json
from .models import BusinessSystem
from django.http import HttpResponse
from mars_api.tools import queryset_to_dict, http_log
import logging

log = logging.getLogger('djangodemo')


# 保存“业务系统”数据
@http_log
def post_business_system(request):
    result = {'status': False}
    try:
        body = request.body  # type:bytes
        params = json.loads(body.decode(encoding='utf-8'))
        business_system = BusinessSystem(system_code=params['systemCode'], system_name=params['systemName'])
        business_system.save()
        result = {'status': True}
    except Exception as ex:
        log.error(ex)
    return HttpResponse(json.dumps(result),
                        content_type="application/json")


# 获取业务系统分页数据
@http_log
def get_business_system_page(request):
    get = request.GET
    page_index = get.get('pageIndex', 1)
    page_size = get.get('pageSize', 10)
    system_code = get.get('systemCode', None)
    system_name = get.get('systemName', None)
    bs_list = BusinessSystem.objects.all()
    if system_code is not None:
        bs_list = bs_list.filter(system_code=system_code)
    if system_name is not None:
        bs_list = bs_list.filter(system_name=system_name)
    count = bs_list.count()
    bs_list = bs_list[(page_index - 1) * page_size:page_index * page_size]
    result = {'pageIndex': page_index, 'pageSize': page_size, 'count': count,
              'data': queryset_to_dict(bs_list)}
    return HttpResponse(json.dumps(result),
                        content_type="application/json")
