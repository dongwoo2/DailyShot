from django.urls import path
from .views import Show

app_name = 'shop'

urlpatterns = [
    path('show/', Show.as_view(), name='show'),
]