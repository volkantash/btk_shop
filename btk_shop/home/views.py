from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from ayarlar.models import Url

# Create your views here.
def index(request):
    #uyg_url = Url.objects.filter(uyg="home")
    #url = get_object_or_404(uyg_url, url=url)
    isim = "Volkan"
    context = {'isim': isim}
    return render(request, 'index.html', context)
    # return HttpResponse("Merhaba")