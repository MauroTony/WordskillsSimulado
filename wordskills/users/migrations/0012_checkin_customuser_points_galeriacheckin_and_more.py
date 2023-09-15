# Generated by Django 4.2.4 on 2023-09-05 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_avaliacoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_base64', models.CharField(blank=True, max_length=1000000, null=True)),
                ('adress', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.CharField(blank=True, max_length=20, null=True)),
                ('long', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='GaleriaCheckin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_base64', models.CharField(blank=True, max_length=1000000, null=True)),
                ('chackin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.checkin')),
            ],
        ),
        migrations.AddField(
            model_name='checkin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
