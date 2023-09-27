from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class Chef(models.Model):
    phone = models.CharField(max_length=255,null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # Chef类中声明了user字段，是onetoonefield,数据库中就会叫“user_id”字段

    def __str__(self) -> str:
        return self.user.username
    
    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name
    
    def username(self):
        return self.user.username


class Menu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    chef = models.OneToOneField(Chef,on_delete=models.CASCADE)  # Menu与Chef是一对一

    def save(self, *args, **kwargs):    # 重写save，解决中文title转slug问题
        if not self.slug:
            self.slug = slugify(self.title)
        super(Menu, self).save(*args, **kwargs)


class MenuImage(models.Model):
    menu = models.OneToOneField(Menu,on_delete=models.CASCADE,related_name='images')
    # image = models.ImageField(upload_to='')   # 待补充



