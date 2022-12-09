from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todo'),
    path('del/<str:id>',views.remove,name='del'),
    ]
