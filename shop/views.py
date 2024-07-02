from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class Show(APIView):
    def get(self, request):
        return render(request, "shop/show.html")

# def show(request):
#     return render(request, 'shop/show.html')