from django.conf.urls import url
from .views import *
urlpatterns = [
    url('^addfavorite/', add_favorite, name='add_favorite'),
    url('^adeletefavorite/', delete_favorite, name='delete_favorite'),
    url('^addcart/', add_cart, name='add_cart'),
    url('^deletecart/', delete_cart, name='delete_cart'),
    url('^changecart/', change_cart, name='change_cart'),
    url('^cartlist/', cart_list, name='cart_list'),
]
