from rest_framework import serializers
from .models import Menu, Chef

# 菜单相关序列化器
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','title','description','chef']   # 模型中OneToOneField叫chef,实际在mysql中叫chef_id

# 大厨相关序列化器
class ChefSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Chef
        fields = ['id','user_id','phone','username']