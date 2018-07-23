from django.contrib import admin
from django.urls import path
from django.urls import include
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls)
]
