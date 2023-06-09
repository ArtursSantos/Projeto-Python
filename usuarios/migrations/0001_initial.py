# Generated by Django 4.1.3 on 2022-11-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('numero', models.IntegerField()),
                ('senha', models.CharField(max_length=64)),
                ('genero', models.CharField(choices=[('M', 'Male'), ('F', 'Famale'), ('O', 'others'), ('N', 'none')], max_length=1)),
            ],
        ),
    ]
