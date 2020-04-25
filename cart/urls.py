from django.conf.urls import url
from .views import view_cart, add_to_cart, update_cart, remove_product


urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^update/(?P<id>\d+)', update_cart, name='update_cart'),
    url(r'^remove/(?P<id>\d+)', remove_product, name='remove_product'),
]
