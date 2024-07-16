from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import AlcolDrinks


# Create your views here.

class CreateAlcol(APIView):
    def post(self, request):
        name = request.data('name', None)
        inventory = request.data('inventory', None)
        price = request.data('price', None)
        alcol_type = request.data('alcol_type', None)
        drink_type = request.data('drink_type', None)

        if AlcolDrinks.objects.filter(name=name).exists():
            return JsonResponse({'status': 'error', 'message': '중복된 데이터입니다.'}, status=400)
        else:
            AlcolDrinks.objects.create(name=name,
                                       inventory=inventory,
                                       price=price,
                                       alcol_type=alcol_type,
                                       drink_type=drink_type)
            return JsonResponse({'status': 'success', 'message': '데이터가 성공적으로 생성되었습니다.'})

class ShowAlcol(APIView):
    def get(self, request): # 여기다가 페이지 적용 또는 밑에 술 계속보이게 웹에서 불러오는 것 처럼
        AllAlcol = AlcolDrinks.objects.all()

        return render(request,'alcoldrinks/showalcol.html', {'AllAlcol': AllAlcol})
