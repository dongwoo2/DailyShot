from django.urls import path
from .views import Show, ShopJoin

app_name = 'shop'

urlpatterns = [
    path('show/', Show.as_view(), name='show'),
    path('shopjoin/', ShopJoin.as_view(), name='shopjoin'),
]