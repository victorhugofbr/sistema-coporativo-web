# Generated by Django 5.1.1 on 2024-10-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, default='perfil/foto-perfil.jpg', upload_to='perfil/foto/'),
        ),
    ]