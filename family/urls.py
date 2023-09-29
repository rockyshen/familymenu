from django.urls import path
from . import views
# from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('menu',views.MenuViewSet)
router.register('chef',views.ChefViewSet)

menu_router = routers.NestedDefaultRouter(router,'menu',lookup='menu')
menu_router.register('images',views.MenuImageViewSet,basename='menu-images')

# URLConf 告诉Django，这个路径去调用
urlpatterns = router.urls + menu_router.urls