from django.shortcuts import render
from .models import *

def index(request):
    future = FutureModel.objects.all()
    future_img = FutureImage.objects.all()
    service = ServiceModel.objects.all()
    team = TeamModel.objects.all()
    portfolio = Portfolio.objects.all()
    image_portfolio = ImagePortfolio.objects.all()

    context = {
        "future": future,
        'future_img': future_img,
        'service': service,
        'team': team,
        'portfolio': portfolio,
        'image_portfolio': image_portfolio

    }
    return render(request, 'index.html', context)

