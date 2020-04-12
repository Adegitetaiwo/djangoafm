"""afm URL Configuration

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
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.sundaySchool, name = 'sunday_school'),
    url(r'^lesson/english/adult/(?P<id>\d+)/$', views.lesson_adult_e, name = 'lesson-adult'),
    url(r'^lesson/english/intermediate/(?P<id>\d+)/$', views.lesson_inter_e, name = 'lesson-inter'),
    url(r'^lesson/english/elementary/(?P<id>\d+)/$', views.lesson_element, name = 'lesson-element'),
    url(r'^lesson/french/adult/(?P<id>\d+)/$', views.lesson_adult_f, name = 'lesson-adult-f'),
    url(r'^lesson/french/intermediate/(?P<id>\d+)/$', views.lesson_inter_f, name = 'lesson-inter-f'),
    url(r'^lesson/yoruba/adult/(?P<id>\d+)/$', views.lesson_adult_y, name = 'lesson-adult-y'),
    url(r'^lesson/yoruba/intermediate/(?P<id>\d+)/$', views.lesson_inter_y, name = 'lesson-inter-y'),
]
