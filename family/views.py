from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Chef, MenuImage
from .serializers import MenuSerializer, ChefSerializer, MenuImageSerializer

# Create your views here.

# 菜单-视图集
class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.prefetch_related('images').all()
    serializer_class = MenuSerializer

# 大厨-视图集
class ChefViewSet(ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer

# 菜单图片-视图集
class MenuImageViewSet(ModelViewSet):
    serializer_class = MenuImageSerializer
    
    def get_serializer_context(self):
        return {'menu_id':self.kwargs['menu_pk']}

    # 重写queryset，获取特定menu的图片
    def get_queryset(self):
        return MenuImage.objects.filter(menu_id=self.kwargs['menu_pk'])