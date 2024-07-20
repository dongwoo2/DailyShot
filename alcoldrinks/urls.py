from django.urls import path

from . import views
from .views import CreateAlcol, ShowAlcol

app_name = 'alcoldrinks'

urlpatterns = [
    #path('', views.index, name='index'),
    path('CreateAlcol', CreateAlcol.as_view(), name='createalcol'),
    path('ShowAlcol', views.ShowAlcol.as_view(), name='showalcol'),
]