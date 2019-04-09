import json
import datetime
from django.db.models import Model, QuerySet


# 将Model转换为字典
def model_to_dict(self):
    if isinstance(self, Model):
        fields = _get_field_name_array(self)
        d = _convert_to_dict(self, fields)
        return d
    else:
        return {}


# 将QuerySet转换为字典
def queryset_to_dict(queryset):
    if isinstance(queryset, QuerySet):
        fields = _get_field_name_array(queryset[0])
        l = []
        for index in range(queryset.count()):
            l.append(_convert_to_dict(queryset[index], fields))
        return l
    else:
        return []


# 获取对象属性名集合
def _get_field_name_array(self):
    fields = []
    for field in self._meta.fields:
        fields.append(field.name)
    return fields


# 将对象按照属性名转换为字典
def _convert_to_dict(self, fields):
    d = {}
    for attr in fields:
        if isinstance(getattr(self, attr), datetime.datetime):
            d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(getattr(self, attr), datetime.date):
            d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
        else:
            d[attr] = getattr(self, attr)
    return d
