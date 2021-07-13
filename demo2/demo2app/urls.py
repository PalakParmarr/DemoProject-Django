
from django.urls import path,include
from demo2app import views
urlpatterns = [
    
    path('', views.index, name='index'),
    path('login/', views.loginU, name='login'),
    path('register/', views.registerU, name='register'),
    
]
