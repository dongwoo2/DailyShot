from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Alcolshop, Filter
from shop.models import AllShop
from .forms import FilterForm
import geocoder

class KakaoMapView(View):
    def get(self, request):
        alcolshops = Alcolshop.objects.all()
        coordinate = geocoder.ip('me').latlng

        # Filter 객체가 없는 경우 기본값으로 생성
        if not Filter.objects.exists():
            Filter.objects.create(patner=True, store=True)  # 기본값 설정

        option = get_object_or_404(Filter)

        form = FilterForm(instance=option)

        if option.patner == False:
            alcolshops = alcolshops.exclude(alcolshoptype='patner')
        if option.store == False:
            alcolshops = alcolshops.exclude(alcolshoptype='store')

        return render(request, "map/kakaomap.html", {'alcolshops': alcolshops, 'form': form, 'coordinate': coordinate})

    def post(self, request):
        option = get_object_or_404(Filter)
        form = FilterForm(request.POST, instance=option)
        if form.is_valid():
            option = form.save(commit=False)
            option.save()
            return redirect('map:kakaomap')

        alcolshops = Alcolshop.objects.all()
        coordinate = geocoder.ip('me').latlng


        if option.patner == False:
            alcolshops = alcolshops.exclude(alcolshoptype='patner')
        if option.store == False:
            alcolshops = alcolshops.exclude(alcolshoptype='store')

        return render(request, "map/kakaomap.html", {'alcolshops': alcolshops, 'form': form, 'coordinate': coordinate})

# urls.py에 다음과 같이 추가:
# from .views import KakaoMapView
# urlpatterns = [
#     path('map/KakaoMap', KakaoMapView.as_view(), name='kakaomap')
# ]
