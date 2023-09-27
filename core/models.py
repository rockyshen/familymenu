from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    # 点击AbstractUser查看默认字段
    # username
    # first_name 这些都是基类默认的字段，继承
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined