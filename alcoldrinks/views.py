import os
from uuid import uuid4

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from mysite.settings import MEDIA_ROOT
from .models import AlcolDrinks


# Create your views here.

class CreateAlcol(APIView):

    def get(self, request):
        return render(request, "alcoldrinks/createalcol.html")

    def post(self, request):
        name = request.POST.get('name')
        inventory = request.POST.get('inventory')
        price = request.POST.get('price')
        alcol_type = request.POST.get('alcol_type')
        drink_type = request.POST.get('drink_type')
        information = request.POST.get('information')
        file = request.FILES.get('file')  # 'file'로 전송된 이미지 파일 가져오기

        print(name,inventory,price,alcol_type,drink_type,information)

        uuid_name = uuid4().hex  # 이미지 파일의 경우 특수문자 한글 막 뒤죽박죽하게 섞여있다 그것을 영어와 숫자로만 적힌 고유id값으로 만들어준다
        save_path = os.path.join(MEDIA_ROOT,
                                 uuid_name)  # 경로지정 경로를 join 미디어루트 경로에 uuid_name을 추가 즉 media/uuid_name 이렇게 지정을 하겠다는 뜻 미디어 폴더에 uuid_name으로 고유값이 만들어진 애까지 지정

        with open(save_path, 'wb+') as destination:  # 실제로 파일을 저장하는 부분
            for chunk in file.chunks():
                destination.write(chunk)

        if AlcolDrinks.objects.filter(name=name).exists():
            return JsonResponse({'status': 'error', 'message': '중복된 데이터입니다.'}, status=400)
        else:
            AlcolDrinks.objects.create(name=name,
                                       inventory=inventory,
                                       price=price,
                                       alcol_type=alcol_type,
                                       drink_type=drink_type,
                                       information=information,
                                       image=uuid_name)
            return JsonResponse({'status': 'success', 'message': '데이터가 성공적으로 생성되었습니다.'}, status=200)


class ShowAlcol(APIView):
    def get(self, request):  # 여기다가 페이지 적용 또는 밑에 술 계속보이게 웹에서 불러오는 것 처럼
        AllAlcol = AlcolDrinks.objects.all()

        return render(request, 'alcoldrinks/showalcol.html', {'AllAlcol': AllAlcol})


class ShowAlcoldetail(APIView):
    def get(self, request, pk):
        detailAlcol = AlcolDrinks.objects.get(pk=pk)

        return render(request,'alcoldrinks/showalcoldetail.html', {'detailAlcol': detailAlcol})