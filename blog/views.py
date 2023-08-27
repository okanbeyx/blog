from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import *


# Create your views here.
def index(request):
    get_object_or_404(Deneyim)
    deneyim = Deneyim.objects.all()
    okul = Okul.objects.all()

    return render(request, 'index.html', {
        'deneyim': deneyim,
        'okul': okul
    })


@login_required
def adin_sayfasi(request):
    # Adın sayfasının içeriğini burada oluşturabilirsiniz
    return render(request, 'adin_sayfasi.html')
