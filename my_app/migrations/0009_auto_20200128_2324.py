# Generated by Django 3.0.2 on 2020-01-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_auto_20200128_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='my_app.Category', verbose_name='Categorias'),
        ),
    ]
