from django.db import models

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.label
    
class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)  # 这里要修改一下，tag删掉，tagitem别删掉