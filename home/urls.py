from django.urls import path
from . import views

urlpatterns = [
    path('get_valid_email/', views.home, name="home"),

]
