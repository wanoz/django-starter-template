from django.urls import path
from django.urls import include, re_path
from django.conf.urls import url
from mt_app import views

# Template tagging
app_name = 'mt'

urlpatterns = [
    path('', views.page_index, name='page_index'),
]