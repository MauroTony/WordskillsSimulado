from rest_framework import serializers
from .models import (CustomUser, Gallery, Avaliacoes,
                     Checkin, GaleriaCheckin, hotels,
                     reclamacoes)
import base64
import re

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "name", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'],
                                       name=validated_data['name'],
                                         )
        user.username = validated_data['username']
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'bio', 'birth_date', 'profile_picture_base64')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'bio', 'birth_date', 'profile_picture_base64', 'is_admin')


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'user', 'images_base64')

    def validate_images_base64(self, value):
        """
        Verifica se a string é um valor válido em base64 e se tem o prefixo de tipo de dados.
        """
        pattern = r'^data:image/.+;base64,'

        if re.match(pattern, value):
            base64_str = re.sub(pattern, '', value)
            try:
                # Verifica se é um valor válido em base64
                base64.b64decode(base64_str)
            except Exception:
                raise serializers.ValidationError("The provided data is not a valid base64 image.")
        elif not value.strip():  # caso a string seja vazia ou só espaços
            raise serializers.ValidationError("The provided data is empty.")
        else:
            try:
                # Tenta decodificar o valor em base64 para garantir que seja válido
                base64.b64decode(value)
            except Exception:
                raise serializers.ValidationError("The provided data is not a valid base64 image.")

        return value

    def create(self, validated_data):
        """
        Remove o prefixo de tipo de dados, se presente, ao criar um novo registro.
        """
        pattern = r'^data:image/.+;base64,'
        images_base64 = validated_data.get('images_base64', '')
        if re.match(pattern, images_base64):
            validated_data['images_base64'] = re.sub(pattern, '', images_base64)

        return super(GallerySerializer, self).create(validated_data)

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = '__all__'

    def validate_image_base64(self, value):
        """
        Verifica se a string é um valor válido em base64 e se tem o prefixo de tipo de dados.
        """
        pattern = r'^data:image/.+;base64,'

        if re.match(pattern, value):
            base64_str = re.sub(pattern, '', value)
            try:
                # Verifica se é um valor válido em base64
                base64.b64decode(base64_str)
            except Exception:
                raise serializers.ValidationError("The provided data is not a valid base64 image.")
        elif not value.strip():  # caso a string seja vazia ou só espaços
            raise serializers.ValidationError("The provided data is empty.")
        else:
            try:
                # Tenta decodificar o valor em base64 para garantir que seja válido
                base64.b64decode(value)
            except Exception:
                raise serializers.ValidationError("The provided data is not a valid base64 image.")

        return value

    def create(self, validated_data):
        """
        Remove o prefixo de tipo de dados, se presente, ao criar um novo registro.
        """
        pattern = r'^data:image/.+;base64,'
        image_base64  = validated_data.get('image_base64', '')
        if re.match(pattern, image_base64 ):
            validated_data['image_base64 '] = re.sub(pattern, '', image_base64 )

        return super(AvaliacaoSerializer, self).create(validated_data)


class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = '__all__'

    def validate_image_base64(self, value):
        """
        Verifica se a string é um valor válido em base64 e se tem o prefixo de tipo de dados.
        """
        pattern = r'^data:image/.+;base64,'

        if re.match(pattern, value):
            base64_str = re.sub(pattern, '', value)
            try:
                # Verifica se é um valor válido em base64
                base64.b64decode(base64_str)
            except Exception:
                raise serializers.ValidationError("The provided data is not a valid base64 image.")
        elif not value.strip():  # caso a string seja vazia ou só espaços
            raise serializers.ValidationError("The provided data is empty.")
        else:
            try:
                # Tenta decodificar o valor em base64 para garantir que seja válido
                base64.b64decode(value)
            except Exception:
                raise serializers.ValidationError("The provided data is not a valid base64 image.")

        return value

    def create(self, validated_data):
        """
        Remove o prefixo de tipo de dados, se presente, ao criar um novo registro.
        """
        pattern = r'^data:image/.+;base64,'
        image_base64  = validated_data.get('image_base64', '')
        if re.match(pattern, image_base64 ):
            validated_data['image_base64 '] = re.sub(pattern, '', image_base64 )

        return super(CheckinSerializer, self).create(validated_data)


class GaleriaCheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = GaleriaCheckin
        fields = '__all__'

    def validate_image_base64(self, value):
        """
        Verifica se a string é um valor válido em base64 e se tem o prefixo de tipo de dados.
        """
        pattern = r'^data:image/.+;base64,'

        if re.match(pattern, value):
            base64_str = re.sub(pattern, '', value)
            try:
                # Verifica se é um valor válido em base64
                base64.b64decode(base64_str)
            except Exception:
                raise serializers.ValidationError("The provided data is not a valid base64 image.")
        elif not value.strip():  # caso a string seja vazia ou só espaços
            raise serializers.ValidationError("The provided data is empty.")
        else:
            try:
                # Tenta decodificar o valor em base64 para garantir que seja válido
                base64.b64decode(value)
            except Exception:
                raise serializers.ValidationError("The provided data is not a valid base64 image.")

        return value

    def create(self, validated_data):
        """
        Remove o prefixo de tipo de dados, se presente, ao criar um novo registro.
        """
        pattern = r'^data:image/.+;base64,'
        images_base64 = validated_data.get('images_base64', '')
        if re.match(pattern, images_base64):
            validated_data['image_base64'] = re.sub(pattern, '', images_base64)

        return super(GaleriaCheckinSerializer, self).create(validated_data)


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotels
        fields = '__all__'


class ReclamacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = reclamacoes
        fields = '__all__'
