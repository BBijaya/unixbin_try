"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from .views import test, BlogHomeView, PostDetailView, TagListView, DebianListView
from .views import UbuntuListView, CentosListView, RedhatListView, ArchLinuxListView, contact
from .views import NewsLetterView
# app_name = 'blog'

urlpatterns = [
    path('', test, name="home"),
    path('blog/', BlogHomeView.as_view(), name="blog_home"),
    path('blog/tag/<slug:tag_slug>/', TagListView.as_view(), name="tag_related"),
    path('blog/<slug:the_slug>/', PostDetailView.as_view(), name="post_detail"),
    path('blog/category/debian/', DebianListView.as_view(), name="debian"),
    path('blog/category/ubuntu/', UbuntuListView.as_view(), name="ubuntu"),
    path('blog/category/centos/', CentosListView.as_view(), name="centos"),
    path('blog/category/redhat/', RedhatListView.as_view(), name="redhat"),
    path('blog/category/archlinux/', ArchLinuxListView.as_view(), name="archlinux"),
    path('newsletter/', NewsLetterView.as_view(), name="newsletter"),
    path('contact/', contact, name="contact"),



]
