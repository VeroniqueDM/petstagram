from django.shortcuts import render, redirect

from petstagram.main_app.models import PetPhoto


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    context = {
        'pk': pk,
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)



def add_pet_photo(request):
    context = {

    }
    return render(request, 'photo_create.html', context)


def edit_photo(request):
    context = {

    }
    return render(request, 'photo_edit.html', context)
