from django.urls import path

from . import views
from .views import KakaoMapView

app_name = 'mapss'

urlpatterns = [
    #path('', views.index, name='index'),
    path('mapss/KakaoMap', KakaoMapView.as_view(), name='kakaomap')
]