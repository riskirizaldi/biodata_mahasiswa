from django.forms import ModelForm
from pribadiapp.models import mahasiswa

class FormMahasiswa(ModelForm):
    class Meta:
      model = mahasiswa
      fields = '__all__'