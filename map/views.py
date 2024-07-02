from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class KakaoMap(APIView):
    def get(self, request):
        return render(request, "map/kakaomap.html")