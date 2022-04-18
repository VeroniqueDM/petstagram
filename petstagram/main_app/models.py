import datetime


from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
from django.utils import timezone

from petstagram.main_app.validators import only_letters_validator, validate_file_size, MinDateValidator, \
    MaxDateValidator


class Profile(models.Model):
    # id/pk by default
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDER_TUPLE = (MALE, FEMALE, DO_NOT_SHOW)
    GENDERS = [(x, x) for x in GENDER_TUPLE]
    FIRST_NAME_MAX_LENGTH =30
    FIRST_NAME_MIN_LENGTH =2
    LAST_NAME_MAX_LENGTH =30
    LAST_NAME_MIN_LENGTH =2
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH)

        ],
        verbose_name="Enter first name",

    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH), # <- This is a class
            only_letters_validator, # <- This is a reference to a function
        ],
        verbose_name="Enter last name",
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name = "Enter URL",
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email_address = models.EmailField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=max(len(x) for (x, _) in GENDERS),
        null=True,
        blank=True,
        choices=GENDERS,
    )

    # @property
    # def age(self):
    #     return datetime.datetime.now().year - self.date_of_birth.year

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Pet(models.Model):
    CAT = 'CAT'
    DOG = "DOG"
    BUNNY = 'BUNNY'
    PARROT = 'PARROT'
    FISH = 'FISH'
    OTHER = 'OTHER'
    PETS_TUPLE = (CAT, DOG, BUNNY, OTHER, PARROT, FISH)
    PETS = [(x, x) for x in PETS_TUPLE]
    NAME_MAX_LENGTH = 30
    MIN_DATE = datetime.date(1920,1,1)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        # unique=True,
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in PETS),
        choices=PETS,
    )
    date_of_birth = models.DateField(
        null=True,
        blank = True,
        validators = (
            MinDateValidator(MIN_DATE),

        )
    )
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    MAX_FILE_SIZE = 5242880
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        # validators = (
        #     validate_file_size,
        # )
    )
    tagged_pets = models.ManyToManyField(
        to=Pet,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    likes = models.IntegerField(
        default=0,
    )