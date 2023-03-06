from django.urls import path
from .views import home, login, register, menu

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('menu/', menu, name='menu')
]