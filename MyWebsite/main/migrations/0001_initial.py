# Generated by Django 4.2.1 on 2023-05-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Brand')),
                ('shoe', models.TextField(verbose_name='Name shoe')),
            ],
        ),
    ]
