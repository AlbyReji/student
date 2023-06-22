from django.forms import ModelForm
from .models import Studentdb


class StudentForm(ModelForm):
    class Meta:
        model = Studentdb
        fields = '__all__'