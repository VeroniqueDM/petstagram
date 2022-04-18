from django.shortcuts import render

from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import PetPhoto


def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pets_photos = set(PetPhoto.objects.filter(tagged_pets__user_profile=profile))
    context = {
        'pets_photos': pets_photos,
    }
    return render(request, 'dashboard.html', context)