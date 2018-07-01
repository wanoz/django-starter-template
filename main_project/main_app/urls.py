from django.urls import path
from django.urls import include, re_path
from django.conf.urls import url
from main_app import views

# Template tagging
app_name = 'main'

urlpatterns = [
    path('', views.page_index, name='page_index'),
]