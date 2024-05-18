from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bolimlar/<int:pk>/ichki-bolimlar/', BolimView.as_view()),
    path('mahsulot/', MahsulotView.as_view(), name='mahsulot'),
]