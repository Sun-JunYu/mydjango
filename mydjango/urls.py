"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from django.views.static import serve
from myapp.views import myindex
from myapp.md_user import Register,Login,MyCode,wb_back,UploadFile,QiNiu

urlpatterns = [
    #定义超链接路由
    re_path('^static/upload/(?P<path>.*)$',serve,{'document_root':'/static/upload/'}),
    path('',myindex),
    path('register/',Register.as_view()),
    path('login/',Login.as_view()),
    path('code/',MyCode.as_view()),
    path('md_admin/weibo/',wb_back),
    path('upload/', UploadFile.as_view()),
    path('qiniu/', QiNiu.as_view()),
]
