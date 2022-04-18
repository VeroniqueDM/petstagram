
from django.urls import path

from petstagram.main_app.views.generic import show_home, show_dashboard
from petstagram.main_app.views.pet_photos import add_pet_photo, edit_photo, show_pet_photo_details, like_pet_photo
from petstagram.main_app.views.pets import add_pet, edit_pet, delete_pet
from petstagram.main_app.views.profiles import show_profile, create_profile, delete_profile, edit_profile

urlpatterns = [
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('pet/add/', add_pet, name='add pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>', delete_pet, name='delete pet'),
    path('photo/add/', add_pet_photo, name='add pet photo'),
    path('photo/edit/<int:pk>/', edit_photo, name='edit photo'),
    path('photo/details/<int:pk>', show_pet_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>', like_pet_photo, name= 'like pet photo'),
]