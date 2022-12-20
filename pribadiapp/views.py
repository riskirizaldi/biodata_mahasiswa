from django.shortcuts import render
from pribadiapp.models import mahasiswa
from pribadiapp.forms import FormMahasiswa

# Create your views here.
def Mahasiswa(request):
    mahasiswas = mahasiswa.objects.all()
    context = {
        'mahasiswas': mahasiswas,
    }
    return render(request,'index.html',context)

def Create(request):
    form = FormMahasiswa()
    
    context = {
        'form': form,
    }
    return render(request,'create.html',context)