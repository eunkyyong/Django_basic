from django.contrib import admin
from django.urls import path
from . import views
# . : 자기 패키지 안에(자신 위치)
# .. : 이전 경로

app_name = 'restaurants'

urlpatterns = [
    path('', views.restaurant, name='restaurant'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'), 
]