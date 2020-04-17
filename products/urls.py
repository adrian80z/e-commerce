from django.conf.urls import url
from .views import get_products, product_details


urlpatterns = [
    url(r'^$', get_products, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$',
        product_details, name="detail"),
]
