from django.urls import path
from .views import KakaoMap

app_name = 'map'

urlpatterns = [
    #path('', views.index, name='index'),
    path('KakaoMap', KakaoMap.as_view(), name='kakao_map'),
]