from django.conf.urls import url
from .views import *
urlpatterns = [
    url('^addorder/', add_order, name='add_order'),
    url('^orderlist/', order_list, name='order_list'),
    url('^cancelorder/', cancel_order, name='cancel_order'),
]
