# modulo_usuario/views.py
from django.contrib.auth import get_user_model
from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (UserSerializer, CustomUserUpdateSerializer,
                          GallerySerializer, CustomUserSerializer,
                          AvaliacaoSerializer, CheckinSerializer,
                            GaleriaCheckinSerializer, HotelsSerializer, ReclamacoesSerializer
                          )
from .models import (CustomUser, Gallery, Avaliacoes,
                     Checkin, GaleriaCheckin, hotels,
                     reclamacoes)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UpdateUserView(generics.UpdateAPIView):
    serializer_class = CustomUserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class CreateGalleryView(generics.CreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticated]


class GalleryRetrieveDeleteView(generics.DestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        gallery = self.get_object()
        if gallery.user_id != request.user.id:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        # Deletar o registro
        gallery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateAvaliacaoView(generics.CreateAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [IsAuthenticated]


class ApproveAvaliacaoView(generics.UpdateAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        avaliacao = self.get_object()

        # Assuming you send status_approved as True or False in the request data
        if request.data.get("status_approved"):
            avaliacao.status_approved = True
            avaliacao.status_pending = False
        else:
            avaliacao.status_approved = False

        avaliacao.save()
        return Response(AvaliacaoSerializer(avaliacao).data)


class ListAvaliacoesView(generics.ListAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [IsAuthenticated]

class AddPointsView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        points_to_add = request.data.get('points')

        if not points_to_add or not isinstance(points_to_add, int):
            return Response({"detail": "Invalid points value"}, status=status.HTTP_400_BAD_REQUEST)

        user.points += points_to_add
        user.save()

        return Response({"points": user.points})


class CreateCheckinView(generics.CreateAPIView):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Vincula o checkin ao usuário atual
        serializer.save(user=self.request.user)


class DeleteCheckinView(generics.DestroyAPIView):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        checkin = self.get_object()
        if checkin.user != request.user:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)

class ListUserCheckinsView(generics.ListAPIView):
    serializer_class = CheckinSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra os Checkins com base no usuário autenticado
        return Checkin.objects.filter(user=self.request.user)


class ListGaleriaCheckinView(generics.ListAPIView):
    serializer_class = GaleriaCheckinSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        checkin_id = self.request.query_params.get('checkin-id')

        # Se checkin_id não for fornecido, retornar uma lista vazia
        if not checkin_id:
            return GaleriaCheckin.objects.none()

        return GaleriaCheckin.objects.filter(checkin__id=checkin_id, checkin__user=self.request.user)

class CreateGaleriaCheckinView(generics.CreateAPIView):
    serializer_class = GaleriaCheckinSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Garanta que o Checkin associado pertence ao usuário atual
        checkin = self.request.data.get('checkin')
        if Checkin.objects.filter(id=checkin, user=self.request.user).exists():
            serializer.save()
        else:
            raise serializers.ValidationError("Checkin does not belong to the user")

class DeleteGaleriaCheckinView(generics.DestroyAPIView):
    serializer_class = GaleriaCheckinSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GaleriaCheckin.objects.filter(checkin__user=self.request.user)


class HotelsCreateView(generics.CreateAPIView):
    queryset = hotels.objects.all()
    serializer_class = HotelsSerializer


class HotelsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = hotels.objects.all()
    serializer_class = HotelsSerializer


# Views para reclamacoes
class ReclamacoesCreateView(generics.CreateAPIView):
    queryset = reclamacoes.objects.all()
    serializer_class = ReclamacoesSerializer


class ReclamacoesUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = reclamacoes.objects.all()
    serializer_class = ReclamacoesSerializer


class HotelsListView(generics.ListAPIView):
    queryset = hotels.objects.all()
    serializer_class = HotelsSerializer


class ReclamacoesListView(generics.ListAPIView):
    queryset = reclamacoes.objects.all()
    serializer_class = ReclamacoesSerializer
