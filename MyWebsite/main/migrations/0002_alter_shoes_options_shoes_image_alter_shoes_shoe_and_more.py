# Generated by Django 4.2.1 on 2023-05-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoes',
            options={'verbose_name': 'Обувь', 'verbose_name_plural': 'Модели'},
        ),
        migrations.AddField(
            model_name='shoes',
            name='image',
            field=models.ImageField(default='', upload_to='shoes/'),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='shoe',
            field=models.CharField(max_length=100, verbose_name='Name shoe'),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Brand'),
        ),
    ]
