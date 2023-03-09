from django.urls import path
from .views import home, login, register, menu, add_to_cart

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('menu/', menu, name='menu'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
]