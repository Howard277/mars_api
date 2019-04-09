from django.db import models


# 通用模型
class GeneralModel(models.Model):
    create_login_name = models.CharField(max_length=50)  # 创建人登录名
    create_time = models.DateTimeField(auto_now=True)  # 创建时间

    class Meta:
        abstract = True
