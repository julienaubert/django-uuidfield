from django.forms import ModelForm
from uuidfield.tests.models import ManualUUIDField


class ManualUUIDForm(ModelForm):
    class Meta:
        model = ManualUUIDField
        fields = ['uuid']
