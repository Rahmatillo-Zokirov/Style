from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bolimlar/<int:pk>/ichki-bolimlar/', BolimView.as_view()),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mahsulotlar/<int:pk>/', MahsulotView.as_view()),
    path('ichki-bolim/<int:pk>/', IchkiBolimMahsulotlarView.as_view(), name='ichki_bolim_mahsulotlar'),
]
