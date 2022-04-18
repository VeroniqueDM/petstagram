from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def only_letters_validator(value):
    for symbol in value:
        if symbol.isalpha():
            continue
        else:
            raise ValidationError('Value must contain letters only.')


def validate_file_size(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError("The maximum file size that can be uploaded is 5MB")
    return validate


@deconstructible
class MinDateValidator:
    def __init__(self,min_date):
        self.min_date = min_date
    def __call__(self,value):
        if value < self.min_date:
            raise ValidationError(f"Date must be greater than {self.min_date}")

@deconstructible
class MaxDateValidator:
    def __init__(self,max_date):
        self.max_date = max_date
    def __call__(self,value):
        if value < self.max_date:
            raise ValidationError(f"Date must be earlier than {self.max_date}")