#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=70)
    #文章正文
    body = models.TextField()
    #文章创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #文章摘要,可为空
    excerpt = models.CharField(max_length=200,blank=True)
    #数据关联方式
    #一对多
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #多对多，可为空
    tags = models.ManyToManyField(Tag,blank=True)

    #作者，一对多关联，User是django用于处理用户注册、登陆等流程的内置用户模型
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']