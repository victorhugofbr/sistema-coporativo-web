# Generated by Django 5.1.1 on 2024-10-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, default='perfil/foto-padrao.jpg', upload_to='perfil/foto/'),
        ),
    ]