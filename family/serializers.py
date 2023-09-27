from rest_framework import serializers
from .models import Menu, Chef, Category


# 大厨相关序列化器
class ChefSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Chef
        fields = ['id','user_id','phone','username']

# 简单大厨信息序列化器
class SimpleChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ['username']

# 类别相关序列化器
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

# 菜单相关序列化器
class MenuSerializer(serializers.ModelSerializer):
    chef = SimpleChefSerializer()
    category = CategorySerializer()
    class Meta:
        model = Menu
        fields = ['id','title','description','chef', 'category']   # 模型中OneToOneField叫chef,实际在mysql中叫chef_id