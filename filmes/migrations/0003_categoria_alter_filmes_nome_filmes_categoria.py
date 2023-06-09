# Generated by Django 4.1.3 on 2022-12-08 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0002_alter_filmes_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='filmes',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='filmes',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='filmes.categoria'),
            preserve_default=False,
        ),
    ]
