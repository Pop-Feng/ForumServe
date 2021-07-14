from django.http import HttpResponse
from django.http import JsonResponse
import json
from ForumServe.models import Userdata,Blog,BlogMessage,Forum,ForumMessage,Questions,QandA


##登录请求
def Login(request):
    # return HttpResponse(json.dumps({'ret':1,'msg':'登录成功'}))
    data = request.GET
    try:
        #根据用户名从数据库中查找用户数据
        user = Userdata.objects.get(username=data['username'])
    except Userdata.DoesNotExist:
        return JsonResponse({'ret':1,'msg':'验证失败'})

    else:
        if user.username == data['username'] and user.password == data['password']:
            return JsonResponse({'ret': 0, 'msg': '登录成功！', 'id': user.id, 'name': user.name})
        else:
            return JsonResponse({'ret': 1, 'msg': '验证失败！'})




##注册请求
def Register(request):
    data = request.GET
    # 从请求消息中 获取要注册的用户信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    try:
        # 根据 id 从数据库中找到相应的客户记录
        user = Userdata.objects.get(username=data['username'])
        # print(user)
    except Userdata.DoesNotExist:
        record = Userdata.objects.create(name=data['name'],
                                         username=data['username'],
                                         password=data['password'])
        # print(record)
        return JsonResponse({
            'ret': 0,
            'msg': '注册成功！'
        })
        # delete 方法就将该记录从数据库中删除了
    return JsonResponse({'ret':1,'msg':'该用户名已被注册！'})



##post接收用户创作的博客
def PostBlog(request):
    result = json.loads(request.body)
    record = Blog.objects.create(blog_title=result['title'],
                                 blog_content=result['content'],
                                 blog_name=result['name'])
    # print(record)
    return JsonResponse({'ret':0,'msg':'发布成功'})

##post接收用户发起的问题
def PostQuesion(request):
    result = json.loads(request.body)
    # record = Questions.objects.create()
    # print(result['title'])
    # print(result['content'])
    # print(result['name'])
    record = Questions.objects.create(question_title=result['title'],
                                      question_content=result['content'],
                                      question_name=result['name'])
    # print(record)
    return JsonResponse({'ret':0,'msg':'发布问题成功'})

## post保存帖子回复
def GetForumMessage(request):
    result = json.loads(request.body)
    # print(result['data'])
    # print(result['name'])
    # print(result['forumid'])
    record = ForumMessage.objects.create(forum_id=result['forumid'],
                                         forum_reviewer=result['name'],
                                         forum_comment=result['data'])
    # print(record)
    return JsonResponse({'ret':0,'mes':'发布帖子回复成功！'})


##接收用户发布的论坛帖子
def PostForum(request):
    data = request.GET
    # print(data['title'])
    # print(data['name'])
    record = Forum.objects.create(forum_title=data['title'],
                                  forum_name=data['name'])
    # print(record)
    return  JsonResponse({'ret':0,'meg':'发布帖子成功！'})





##发送所有的帖子信息
def GetForum(request):
    qs = Forum.objects.values()
    retlist = list(qs)
    return  JsonResponse({'ret':0,'retlist':retlist})

##发送所有的问答信息
def GetQuestion(request):
    qs = Questions.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret':0,'retlist':retlist})

##获取所有blog的信息
def GetBlog(request):
    qs = Blog.objects.values()
    # print(qs)
    retlist = list(qs)
    return JsonResponse({'ret':0,'retlist':retlist})



##获取博客详情
def GetBlogDetail(request):
    data = request.GET
    # print(data['id'])
    blogdatail = Blog.objects.filter(id = data['id']).values()
    # print(blogdatail)
    retlist = list(blogdatail)
    # print(retlist)
    return JsonResponse({'ret':0,'retlist':retlist})

##获取论坛详情
def GetForumDetail(request):
    data = request.GET
    # print(data['forumid'])
    forumdetail = Forum.objects.filter(id =data['forumid']).values()
    # print(forumdetail)
    retlist = list(forumdetail)
    return JsonResponse({'ret':0,'retlist':retlist})

##获取回答详情
def GetQuestionDetail(request):
    data = request.GET
    # print(data['Questionid'])
    questiondetail = Questions.objects.filter(id=data['Questionid']).values()
    retlist = list(questiondetail)
    return JsonResponse({'ret':0,'retlist':retlist})

##保存博客区评论
def GetBlogMessage(request):
    data = request.GET
    # print(data['blogid'])
    # print(data['name'])
    # print(data['message'])
    record = BlogMessage.objects.create(blog_id=data['blogid'],
                                     blog_reviewer=data['name'],
                                     comment=data['message'])
    return JsonResponse({'ret':0,'msg':'发布成功'})


##保存问答区评论
def GetQuestionMessage(request):
    data = request.GET
    # print(data)
    record = QandA.objects.create(question_id=data['Questionid'],
                                  answer_name=data['name'],
                                  answer_content=data['content'])
    # print(record)
    return JsonResponse({'ret':0,'msg':'发布回答成功'})


##发送博客区评论消息
def SendBlogMessage(request):
    data = request.GET
    # print(data['blogid'])
    blogmessage = BlogMessage.objects.filter(blog_id=data['blogid']).values()
    # print(blogmessage)
    retlist = list(blogmessage)
    return  JsonResponse({'ret':0,'retlist':retlist})

##发送论坛区回复信息
def SendForumMessage(request):
    data = request.GET
    # print(data['forumid'])
    forummessage = ForumMessage.objects.filter(forum_id=data['forumid']).values()
    # print(forummessage)
    retlist = list(forummessage)
    return  JsonResponse({'ret':0,'retlist':retlist})


def SendQuestionMessage(request):
    data = request.GET
    # print(data['Questionid'])
    questionmessage = QandA.objects.filter(question_id=data['Questionid']).values()
    retlist = list(questionmessage)
    return JsonResponse({'ret':0,'retlist':retlist})


