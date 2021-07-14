from django.urls import path
from uploadfileapp import views

urlpatterns = [
    path('', views.index),
    path('model_form_upload/', views.model_form_upload),
    path('list/', views.list)
    ]
