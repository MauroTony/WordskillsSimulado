# modulo_usuario/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        if not username:
            raise ValueError('Username is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=200, unique=True)
    bio = models.CharField(max_length=250, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture_base64 = models.CharField(max_length=1000000, null=True, blank=True)
    points = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Gallery(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=False)
    images_base64 = models.CharField(max_length=1000000, null=True, blank=True)


class Avaliacoes(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=False)
    image_base64 = models.CharField(max_length=1000000, null=True, blank=True)
    nota = models.IntegerField(null=True, blank=True)
    comentario = models.CharField(max_length=1000000, null=True, blank=True)
    data = models.DateField(null=True, blank=True, auto_now_add=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    local = models.CharField(max_length=150, null=True, blank=True)
    user_name = models.CharField(max_length=150, null=True, blank=True)
    status_pending = models.BooleanField(default=True)
    status_approved = models.BooleanField(default=False)

class Checkin(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=False)
    image_base64 = models.CharField(max_length=1000000, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=20, null=True, blank=True)
    long = models.CharField(max_length=20, null=True, blank=True)

class GaleriaCheckin(models.Model):

    checkin = models.ForeignKey(Checkin, on_delete=models.CASCADE, unique=False)
    image_base64 = models.CharField(max_length=1000000, null=True, blank=True)


class hotels(models.Model):

    hotel_name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image_base64 = models.CharField(max_length=1000000, null=True, blank=True)
    lat = models.CharField(max_length=20, null=True, blank=True)
    long = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)

class reclamacoes(models.Model):

    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    