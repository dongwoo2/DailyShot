from django.shortcuts import render
from rest_framework.views import APIView
from backend.mapss.models import Alcolshop
from rest_framework.response import Response
# Create your views here.

class Show(APIView):
    def get(self, request):
        return render(request, "shop/show.html")

class ShopJoin(APIView):
    def get(self, request):
        return render(request, "shop/join.html")

    def post(self, request):
        # TODO 회원가입
        name = request.data.get('name', None)
        location = request.data.get('location', None)
        latitude = request.data.get('latitude', None)
        longitude = request.data.get('longitude', None)
        alcolshoptype = request.data.get('alcolshoptype', None)

        Alcolshop.objects.create(name=name,
                            location=location,
                            latitude=latitude,
                            longitude=longitude,
                            alcolshoptype=alcolshoptype)

        return Response(status=200)



# def show(request):
#     return render(request, 'shop/show.html')