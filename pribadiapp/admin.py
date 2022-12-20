from django.contrib import admin
from pribadiapp.models import mahasiswa
# Register your models here.

class DataMahasiswa(admin.ModelAdmin):
    list_display = ['name', 'alamat', 'tanggal_lahir']
    search_fields = ['name', 'alamat', 'tanggal_lahir']
    list_per_page = 8
    
admin.site.register(mahasiswa, DataMahasiswa)