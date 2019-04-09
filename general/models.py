from django.db import models
from mars_api.models import GeneralModel


# Create your models here.
# 用户模型
class User(GeneralModel):
    login_name = models.CharField(max_length=50, primary_key=True)  # 登录名
    password = models.CharField(max_length=50)  # 密码
    real_name = models.CharField(max_length=20)  # 真实姓名

    class Meta:
        indexes = [
            models.Index(fields=['real_name'])
        ]


# 业务系统模型
class BusinessSystem(GeneralModel):
    system_code = models.CharField(max_length=50, primary_key=True)  # 业务系统编码
    system_name = models.CharField(max_length=50)  # 业务系统名称


# 资源模型
class Resource(GeneralModel):
    system_code = models.CharField(max_length=50)  # 资源所属业务系统编码
    resource_code = models.CharField(max_length=40)  # 资源编码
    resource_name = models.CharField(max_length=40)  # 资源名称
    resource_path = models.CharField(max_length=200)  # 资源路径

    class Meta:
        unique_together = ('system_code', 'resource_code')  # 定义唯一索引
        indexes = [
            models.Index(fields=['system_code', 'resource_code'])
        ]


# 用户角色
class Role(GeneralModel):
    system_code = models.CharField(max_length=50)  # 资源所属业务系统编码
    role_code = models.CharField(max_length=50)  # 角色编码
    role_name = models.CharField(max_length=50)  # 角色名称

    class Meta:
        unique_together = ('system_code', 'role_code')  # 定义唯一索引
        indexes = [
            models.Index(fields=['role_name'])
        ]


# 用户角色关系表
class UserRole(GeneralModel):
    login_name = models.CharField(max_length=50)  # 登录名
    system_code = models.CharField(max_length=50)  # 资源所属业务系统编码
    role_code = models.CharField(max_length=50)  # 角色编码

    class Meta:
        unique_together = ('login_name', 'system_code', 'role_code')  # 定义唯一索引


# 角色资源关系表
class RoleResource(GeneralModel):
    resource_code = models.CharField(max_length=40)  # 资源编码
    system_code = models.CharField(max_length=50)  # 资源所属业务系统编码
    role_code = models.CharField(max_length=50)  # 角色编码

    class Meta:
        unique_together = ('resource_code', 'system_code', 'role_code')  # 定义唯一索引
