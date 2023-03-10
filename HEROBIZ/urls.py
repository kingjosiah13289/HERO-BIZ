"""HEROBIZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='my-index'),
    path('index-2/', views.index_2, name='my-index-2'),
    path('index-3/', views.index_2, name='my-index-3'),
    path('index-4/', views.index_4, name='my-index-4'),
    path('inner-page/', views.inner_page, name='my-inner-page'),
    path('portfolio-details/', views.portfolio_details, name='my-portfolio-details'),
    path('blog/', views.blog, name='my-blog'),
    path('blog-details/', views.blog_details, name='my-blog-details'),
]
