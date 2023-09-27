from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from family.models import Chef

class UserCreateSerializer(BaseUserCreateSerializer):
    # 重写save()
    def save(self,**kwargs):
        user = super().save(**kwargs)
        Chef.objects.create(user=user)

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','password']