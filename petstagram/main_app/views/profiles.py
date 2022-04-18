from django.shortcuts import render, redirect

from petstagram.main_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import Pet, PetPhoto, Profile


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects.filter(user_profile=profile)
    pet_photos_count = len(set(PetPhoto.objects.filter(user_profile=profile)))
    pet_photos_likes = sum([photo.likes for photo in set(PetPhoto.objects.filter(user_profile=profile))])
    context = {
        'profile': profile,
        'pet_photos_count': pet_photos_count,
        'pet_photos_likes': pet_photos_likes,
        'pets': pets,
    }
    return render(request, 'profile_details.html', context)


def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        profile_form = form_class(request.POST, instance=instance)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(success_url)

    context = {
        'profile_form': form_class(instance=instance),
    }
    return render(request, template_name, context)


def create_profile(request):
    return profile_action(request, CreateProfileForm, 'index', Profile(), 'profile_create.html')


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'profile', get_profile(), 'profile_edit.html')

# def create_profile(request):
#     if request.method == 'POST':
#         profile_form = CreateProfileForm(request.POST)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect('index')
#
#     context = {
#         'profile_form': CreateProfileForm(),
#     }
#     return render(request, 'profile_create.html', context)

#
# def edit_profile(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         profile_form = EditProfileForm(request.POST, instance=profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect('profile')
#     else:
#         profile_form = EditProfileForm(instance=profile)
#     context = {
#         'profile': profile,
#         'profile_form': profile_form,
#     }
#     return render(request, 'profile_edit.html', context)
#

def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'profile_delete.html')
