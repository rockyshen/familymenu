from django.urls import path
from . import views

# URLConf 告诉Django，这个路径去调用say_hello()这个方法
urlpatterns = [
    path('hello/',views.HelloView.as_view())  # 这里没有括号,因为不是call this function，只是传参
]