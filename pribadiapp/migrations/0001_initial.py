# Generated by Django 4.1.3 on 2022-12-15 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=100)),
                ('tanggal_lahir', models.CharField(max_length=50)),
            ],
        ),
    ]