from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from orderApp.models import Savat, SavatMahsulot
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
class IchkiBolimMahsulotlarView(View):
    def get(self, request, pk):
        ichkiBolim = get_object_or_404(IchkiBolim, id=pk)
        mahsulotlar = Mahsulot.objects.filter(ichki_bolim=ichkiBolim)
        context = {
            'mahsulotlar': mahsulotlar,
            'ichkiBolim': ichkiBolim
        }
        return render(request, 'page-listing-grid.html', context)


class MahsulotlarView(View):
    def get(self, request):
        listing = request.GET.get('listing', None)
        mahsulotlar = Mahsulot.objects.all()
        context = {
            "mahsulotlar": mahsulotlar
        }
        if listing is not None and listing == "large":
            return render(request, 'page-listing-large.html', context)
        else:
            return render(request, 'page-listing-grid.html', context)


class MahsulotView(View):
    def get(self, request, pk):
        mahsulot = get_object_or_404(Mahsulot, id=pk)
        chegirma_narx = f"{mahsulot.narx * (100 - mahsulot.chegirma) / 100:.2f}"
        baholashlar = Baholash.objects.filter(mahsulot=mahsulot)
        baho_foiz = float(mahsulot.baho) / 5 * 100
        context = {
            "mahsulot": mahsulot,
            "chegirma_narx": chegirma_narx,
            "baholashlar": baholashlar,
            "review": len(baholashlar),
            "baho_foiz": baho_foiz
        }
        return render(request, 'page-detail-product.html', context)

    def post(self, request, pk):
        if request.Post.get('type') == "savat":
            mahsulot = get_object_or_404(Mahsulot, id=pk)
            Baholash.objects.create(
                mahsulot=mahsulot,
                user=request.user,
                baho=request.POST.get('baho'),
                izoh=request.POST.get('izoh', None),
            )
            baho = Baholash.objects.filter(mahsulot=mahsulot).aggregate(Avg('baho')).get('baho__avg')
            mahsulot.baho = baho
            mahsulot.save()
            return redirect(f'/mahsulotlar/{mahsulot.id}/')
        elif request.Post.get('type') == "savat":
            mahsulot = get_object_or_404(Mahsulot, id=pk)
            miqdor = request.POST.get('miqdor', None)
            savatlar = Savat.objects.filter(user=request.user)
            if len(savatlar) == 0:
                savat = Savat.objects.create(user=request.user)
            else:
                savat = savatlar.first()
            savatMahsulot = SavatMahsulot.objects.create(
                savat=savat,
                mahsulot=mahsulot,
                miqdor=miqdor
            )
            return redirect(f'/mahsulotlar/{mahsulot.id}/')
