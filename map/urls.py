from django.urls import path

from . import views
from .views import KakaoMapView

app_name = 'map'

urlpatterns = [
    #path('', views.index, name='index'),
    path('map/KakaoMap', KakaoMapView.as_view(), name='kakaomap')
]