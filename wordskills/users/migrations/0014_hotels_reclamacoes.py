# Generated by Django 4.2.4 on 2023-09-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_rename_chackin_galeriacheckin_checkin'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('image_base64', models.CharField(blank=True, max_length=1000000, null=True)),
                ('lat', models.CharField(blank=True, max_length=20, null=True)),
                ('long', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('adress', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='reclamacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
