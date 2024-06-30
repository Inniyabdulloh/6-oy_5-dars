from django.shortcuts import render
from django.views import View
from .models import HomePageBackground, Services, CaruselImages, ReklomCard


# Create your views here.

class HomePageView(View):
    def get(self, request):
        homepage_background = HomePageBackground.objects.get(pk=1)
        carusel_images = CaruselImages.objects.all()
        reklom_card = ReklomCard.objects.all()
        services = Services.objects.all()

        context = {
            'homepage_background': homepage_background,
            'carusel_images': carusel_images,
            'reklom_card': reklom_card,
            'services': services
        }


        return render(request, 'hotel/index.html', context)