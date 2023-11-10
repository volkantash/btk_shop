from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from ayarlar.models import Url

# Create your views here.
def index(request, url="product"):
    uyg_url = Url.objects.filter(uyg="product")
    url = get_object_or_404(uyg_url, url=url)
    return HttpResponse("ürünler")