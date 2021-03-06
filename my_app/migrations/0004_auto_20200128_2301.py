# Generated by Django 3.0.2 on 2020-01-28 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20200128_2249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Artigo', 'verbose_name_plural': 'Artigos'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Sub-título'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
    ]
