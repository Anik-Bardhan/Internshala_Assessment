from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.taskAll, name='all'),
    path('new/', views.taskNew, name='new'),
]
