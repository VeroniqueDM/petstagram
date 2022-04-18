from dashboard.application import forms
from django.core.exceptions import ValidationError

from petstagram.main_app.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

class BootstrapMixin:
    fields = {}
    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


class DisabledFieldsFormMixin:
    disabled_fields = ()
    def _init_disabled_fields(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['readonly'] = 'readonly'


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value Must be positive')