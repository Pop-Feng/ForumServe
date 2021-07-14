"""ForumServe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ForumServe import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.Login),
    path ('register/',views.Register),
    path('postblog/',views.PostBlog),
    path('getblog/',views.GetBlog),
    path('getlogetail/',views.GetBlogDetail),
    path('getblogmessage/',views.GetBlogMessage),
    path('sendblogmessage/',views.SendBlogMessage),
    path('postforum/',views.PostForum),
    path('getforum/',views.GetForum),
    path('getforummessage/',views.GetForumMessage),
    path ('getforumdetail/',views.GetForumDetail),
    path('sendforummessage/',views.SendForumMessage),
    path('postquesion/',views.PostQuesion),
    path('getquestion/',views.GetQuestion),
    path('getquestionmessage/',views.GetQuestionMessage),
    path('getquestiondetail/',views.GetQuestionDetail),
    path('sendquestionmessage/',views.SendQuestionMessage)


]
