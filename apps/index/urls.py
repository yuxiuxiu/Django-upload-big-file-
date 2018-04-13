"""DjangoChunkedUploadDemo URL Configuration

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
from django.urls import path,include
from django.views.generic import RedirectView
from apps.index import views
urlpatterns = [
    path('api/', views.p_api),           # 返回接口数据
    path('api_html/', views.p_html),    # 返回页面渲染
    path('', views.upload),              # 分片上传---先传到服务器内存，在进行分片写入服务器文件
]
