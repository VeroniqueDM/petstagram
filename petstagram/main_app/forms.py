



from django import forms
from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date

from petstagram.main_app.helpers import BootstrapMixin, DisabledFieldsFormMixin
from petstagram.main_app.models import Profile, Pet, PetPhoto
from petstagram.main_app.views import pets


class CreateProfileForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = (
            'first_name', 'last_name', 'profile_picture',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder':"Enter first name",
                },


            ),
            'last_name':forms.TextInput(
                attrs={
                    'placeholder':"Enter last name",
                },

            ),
            'profile_picture':forms.TextInput(
                attrs={
                    'placeholder':"Enter URL"
                },

            ),
        }


class EditProfileForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': "Enter first name",
                },
            ),
            'last_name':forms.TextInput(
                attrs={
                    'placeholder': "Enter last name",
                },
            ),
            'profile_picture': forms.TextInput(
                attrs={
                    'placeholder': "Enter URL"
                },
            ),
            # 'date_of_birth': forms.SelectDateWidget(
            #     attrs={
            #         'min': '1920-01-01', # NOT WORKING
            #     }
            # ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': "Enter email"
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': "Enter description",
                    'rows': 3,
                },
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreatePetForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        # self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Pet
        fields = (
            'name', 'type', 'date_of_birth',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
        }



class EditPetForm(BootstrapMixin, forms.ModelForm):
    # MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    # MAX_DATE_OF_BIRTH = date.today()
    #
    # def clean_date_of_birth(self):
    #     date_of_birth = self.cleaned_data['date_of_birth']
    #     if date_of_birth<self.MIN_DATE_OF_BIRTH or date_of_birth>self.MAX_DATE_OF_BIRTH:
    #         raise ValidationError(f'Date must be between {self.MIN_DATE_OF_BIRTH} and {self.MAX_DATE_OF_BIRTH})')
    #     return date_of_birth

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        # self.initial['gender'] = Profile.DO_NOT_SHOW


    class Meta:
        model = Pet
        fields = (
            'name', 'type', 'date_of_birth',
        )

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
        }
class DeletePetForm(BootstrapMixin,DisabledFieldsFormMixin,forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):

        self.instance.delete()
        return self.instance


    class Meta:
        model = Pet
        fields = (
            'name', 'type', 'date_of_birth',
        )
