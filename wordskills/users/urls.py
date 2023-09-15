# modulo_usuario/urls.py
from django.urls import path
from .views import (RegisterView, CurrentUserView, UpdateUserView,
                    CreateGalleryView, GalleryRetrieveDeleteView, ListAvaliacoesView,
                    CreateAvaliacaoView, ApproveAvaliacaoView, AddPointsView,
                    CreateCheckinView, DeleteCheckinView, ListUserCheckinsView,
                    ListGaleriaCheckinView, CreateGaleriaCheckinView, DeleteGaleriaCheckinView,
                    ReclamacoesCreateView, ReclamacoesUpdateDeleteView, HotelsCreateView,
                    HotelsUpdateDeleteView, HotelsListView, ReclamacoesListView
                    )

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', CurrentUserView.as_view(), name='current-user'),
    path('update-user/', UpdateUserView.as_view(), name='update-user'),
    path('add-gallery/', CreateGalleryView.as_view(), name='create-gallery'),
    path('delete-gallery/<int:pk>/', GalleryRetrieveDeleteView.as_view(), name='delete-gallery'),
    path('avaliacoes/', ListAvaliacoesView.as_view(), name='list-avaliacoes'),
    path('avaliacoes/create/', CreateAvaliacaoView.as_view(), name='create-avaliacao'),
    path('avaliacoes/approve/<int:pk>/', ApproveAvaliacaoView.as_view(), name='approve-avaliacao'),
    path('add-points/', AddPointsView.as_view(), name='add-points'),
    path('checkin/', CreateCheckinView.as_view(), name='create-checkin'),
    path('checkin/<int:pk>/', DeleteCheckinView.as_view(), name='delete-checkin'),
    path('list-checkin/', ListUserCheckinsView.as_view(), name='list-checkin'),
    path('galeria-checkins/', ListGaleriaCheckinView.as_view(), name='list-galeria-checkins'),
    path('galeria-checkins/add/', CreateGaleriaCheckinView.as_view(), name='add-galeria-checkin'),
    path('galeria-checkins/<int:pk>/', DeleteGaleriaCheckinView.as_view(), name='delete-galeria-checkin'),
    path('hotels/', HotelsListView.as_view(), name='hotels-list'),
    path('hotels/create/', HotelsCreateView.as_view(), name='hotels-create'),
    path('hotels/<int:pk>/', HotelsUpdateDeleteView.as_view(), name='hotels-update-delete'),
    path('reclamacoes/', ReclamacoesListView.as_view(), name='reclamacoes-list'),
    path('reclamacoes/create/', ReclamacoesCreateView.as_view(), name='reclamacoes-create'),
    path('reclamacoes/<int:pk>/', ReclamacoesUpdateDeleteView.as_view(), name='reclamacoes-update-delete'),
]
