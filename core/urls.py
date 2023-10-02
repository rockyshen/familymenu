from django.views.generic import TemplateView
from django.urls import path
from .views import index

urlpatterns = [
    path('',index,name='index')  # 首页！
]