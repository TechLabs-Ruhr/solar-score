from . import views     # it means - 'from all import views'
from django.urls import path
from django.contrib import admin
from django.urls import include,path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.index, name='index'),
    path('add',views.addition, name='add'),
    path('sub',views.subtraction, name='sub'),
    path('multi',views.multiplication, name='multi'),
    path('div',views.division, name='div'),

]

# whenever 'localhost:8000' will be called, function named 'index' will be called that is present in 'views.py' file
# This will happen for all other routes as well