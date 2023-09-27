from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Chef
from .serializers import MenuSerializer, ChefSerializer

# Create your views here.

# 菜单-视图集
class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# 大厨-视图集
class ChefViewSet(ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer