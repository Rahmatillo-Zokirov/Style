from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        bolimlar = Bolim.objects.all()[:7]
        context = {
            'bolimlar': bolimlar
        }
        return render(request, 'page-index.html', context)



class BolimlarView(View):
    pass


class BolimView(View):
    def get(self, request, pk):
        bolim = get_object_or_404(Bolim, id=pk)
        ichki_bolimlar = IchkiBolim.objects.filter(bolim=bolim)
        context = {
            'bolim': bolim,
            'ichki_bolimlar': ichki_bolimlar
        }
        return render(request, 'page-category.html', context)

#
# class IchkiBolimMahsulotlarView(View):
#     def get(self, request, pk):
#         ichkiBolim = get_object_or_404(IchkiBolim, id=pk)
#         mahsulotlar = Mahsulot.objects.filter(ichki_bolim=ichkiBolim)
#         context = {
#             'mahsulotlar': mahsulotlar,
#             'ichkiBolim': ichkiBolim
#         }
#         return render(request, 'page-listing-grid.html', context)


class MahsulotView(View):
    def get(self, request):
        return render(request, 'page-detail-product.html')