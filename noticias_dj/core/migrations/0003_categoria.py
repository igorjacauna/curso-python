# Generated by Django 2.0.2 on 2018-02-20 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180220_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
    ]
