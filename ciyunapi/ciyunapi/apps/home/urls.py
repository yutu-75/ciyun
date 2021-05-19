"""ciyunapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include,re_path
from . import views

# import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    path('ciyun/', views.CiyunView.as_view(), name='ciyun'),
    path('update/', views.UpdateView.as_view(), name='update'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('template/', views.TemplateView.as_view(), name='template'),
    re_path('download/(?P<p_name>.*?)/', views.file_down, name="download"),



    path(r'home/banner/', views.BannerView.as_view()),
    path(r'home/nav/', views.NavView.as_view()),
    path(r'home/bottom/', views.BottomView.as_view())
    # path('modify/', views.modify),
    # path('async/', views.ay),
    # path('asyncio/', views.http_call_async),
    # path(r'/', jsonrpc_site.dispatch, name='jsonrpc_mountpoint'),
    # path(r'json/', jsonrpc_site.dispatch, name='jsonrpc_mountpoint'),
    # path('download/(?P<id>\d+)',views.UpdateView.as_view(), name='download'),
]
