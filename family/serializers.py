from rest_framework import serializers
from .models import Menu, Chef, Category, MenuImage


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

class MenuImageSerializer(serializers.ModelSerializer):
    # menu_id必须，但是不用手动填，通过context从URL中获取
    def create(self, validated_data):
        menu_id = self.context['menu_id']
        return MenuImage.objects.create(menu_id=menu_id,**validated_data)
    
    class Meta:
        model = MenuImage
        fields = ['id','image']

# 菜单相关序列化器
class MenuSerializer(serializers.ModelSerializer):
    chef = SimpleChefSerializer()
    category = CategorySerializer()
    images = MenuImageSerializer(read_only=True)
    class Meta:
        model = Menu
        fields = ['id','title','description','images','chef', 'category']   # 模型中OneToOneField叫chef,实际在mysql中叫chef_id