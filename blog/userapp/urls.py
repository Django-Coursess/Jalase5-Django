from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home),
    path('name/', views.name),

    path("app1",views.app1),
    path("blog/",views.app2),
]