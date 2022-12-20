from django.contrib import admin
from django.urls import path
from pribadiapp.views import Mahasiswa, Create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Mahasiswa,name="home"),
    path('create/', Create,name="create"),
]
