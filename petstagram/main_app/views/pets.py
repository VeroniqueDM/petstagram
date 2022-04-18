from django.shortcuts import render, redirect

from petstagram.main_app.forms import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import Pet


def pet_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        profile_form = form_class(request.POST, instance=instance)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(success_url)

    context = {
        'profile_form': form_class(instance=instance),
        'pet':instance,
    }
    return render(request, template_name, context)

def add_pet(request):
    return pet_action(request, CreatePetForm, 'profile', Pet(user_profile=get_profile()), 'pet_create.html')
    # if request.method == "POST":
    #     pet_form = PetForm(request.POST)
    #     if pet_form.is_valid():
    #         pet_form.save()
    #         return redirect('profile')
    # pet_form = PetForm()
    # context = {
    #     'pet_form': pet_form
    # }
    # return render(request, 'pet_create.html', context)

def edit_pet(request, pk):
    return pet_action(request, EditPetForm, 'profile', Pet.objects.get(pk=pk), 'pet_edit.html')
# def edit_pet(request, pk):
#
#     # return pet_action
#     form = EditPetForm()
#     pet = Pet.objects.get(pk=pk)
#     context = {
#         'pk': pk,
#         'pet': pet,
#         'form': form,
#     }
#     return render(request, 'pet_edit.html', context)


def delete_pet(request, pk):
    return pet_action(request, DeletePetForm, 'profile', Pet.objects.get(pk=pk), 'pet_delete.html')
