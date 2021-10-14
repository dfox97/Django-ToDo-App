from django.urls import path

from . import views
#app_name defaul django variablle name ??

urlpatterns = [
    path('', views.index, name='list'),
    path('update/<str:pk>/', views.updateTask, name="update"),
    path('delete/<str:pk>/', views.deleteTask, name="delete")
]
