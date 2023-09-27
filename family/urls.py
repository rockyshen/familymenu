from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('menu',views.MenuViewSet)
router.register('chef',views.ChefViewSet)

# URLConf 告诉Django，这个路径去调用
urlpatterns = router.urls