
from django.urls import path,include
from FormDemoApp import views
urlpatterns = [
    path('', views.mainform),
    path('rform/', views.mainform)
]
