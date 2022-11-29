from django.urls import path
from authoptimuz import views

urlpatterns = [
    path('', views.Home, name="Home")
]