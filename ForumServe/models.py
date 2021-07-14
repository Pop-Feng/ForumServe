from django.db import models

#用户信息表
class Userdata(models.Model):
    #用户名
    username = models.CharField(max_length=15)
    #密码
    password = models.CharField(max_length=15)
    #名称
    name = models.CharField(max_length=20)


#博客表
import datetime
class Blog(models.Model):
    #博客标题
    blog_title = models.CharField(max_length=100,null=True,blank=True)
    #博客内容
    blog_content = models.CharField(max_length=100000,null=True,blank=True)
    #发布者名称
    blog_name = models.CharField(max_length=100,null=False,blank=True)
    #博客发布创建时间
    release_time = models.DateTimeField(default=datetime.datetime.now)


#问答表
import  datetime
class Questions(models.Model):
    #问题标题
    question_title = models.CharField(max_length=100,null=False,blank=True)
    #问题内容
    question_content = models.CharField(max_length=100000,null=True,blank=True)
    #发布问题者的名称
    question_name = models.CharField(max_length=100,null=False,blank=True)
    #问题发布的时间
    question_date = models.DateTimeField(default=datetime.datetime.now)

##论坛表
class Forum(models.Model):
    #论坛标题
    forum_title = models.CharField(max_length=100,null=True,blank=True)
    #论坛发布者名称
    forum_name = models.CharField(max_length=100,null=False,blank=True)
    #论坛创建时间
    release_time = models.DateTimeField(default=datetime.datetime.now)


#问答详情的回答表
import datetime
class QandA(models.Model):
    ##该问题的ID
    question_id = models.CharField(max_length=100,null=False,blank=True)
    ##回答人名称
    answer_name = models.CharField(max_length=100,null=False,blank=True)
    #回答内容
    answer_content = models.CharField(max_length=100,null=False,blank=True)
    #回答时间
    answer_date = models.DateTimeField(default=datetime.datetime.now)

##论坛回复表
class ForumMessage(models.Model):
    ##论坛id
    forum_id = models.CharField(max_length=1000,null=False)
    ##论坛回复人昵称
    forum_reviewer = models.CharField(max_length=1000,null=False)
    #论坛回复内容
    forum_comment = models.CharField(max_length=1000,null=False)



##博客区评论表
class BlogMessage(models.Model):
    #博客id
    blog_id = models.CharField(max_length=1000,null=False)
    #评论人呢称
    blog_reviewer = models.CharField(max_length=1000,null=False)
    #评论内容
    comment = models.CharField(max_length=1000,null=False)



##python manage.py migrate

##python manage.py makemigrations