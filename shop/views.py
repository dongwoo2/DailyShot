from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from map.models import Alcolshop
import json
from rest_framework.response import Response
# Create your views here.

class Show(APIView):
    def get(self, request):
        return render(request, "shop/show.html")

class ShopJoin(APIView):
    def get(self, request):
        return render(request, "shop/shopjoin.html")

    def post(self, request):
        # TODO 입점
        name = request.data.get('name', None)
        location = request.data.get('location', None)
        latitude = request.data.get('latitude', None)
        longitude = request.data.get('longitude', None)
        alcolshoptype = request.data.get('alcolshoptype', None)

        if Alcolshop.objects.filter(name=name, location=location).exists():
            return JsonResponse({'status': 'error', 'message': '중복된 데이터입니다.'}, status=400)
        else:
            Alcolshop.objects.create(name=name,
                                location=location,
                                latitude=latitude,
                                longitude=longitude,
                                alcolshoptype=alcolshoptype)
            return JsonResponse({'status': 'success', 'message': '데이터가 성공적으로 생성되었습니다.'})

        #return Response(status=200)



# def show(request):
#     return render(request, 'shop/show.html')