from django.urls import path
from .views import home, login, register, menu, add_to_cart, cart, remove_from_cart

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('menu/', menu, name='menu'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),
]