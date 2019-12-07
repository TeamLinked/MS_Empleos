from .models import Usuario, Empleo, Postulacion, Categoria
from .serializers import UsuarioSerializer, EmpleoSerializer, PostulacionSerializer, CategoriaSerializer,VerPostulacionSerializer
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import generics

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer



class EmpleoList(generics.ListCreateAPIView):
    queryset = Empleo.objects.all()
    serializer_class = EmpleoSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id_ofertante', 'titulo', 'categoria']

class EmpleoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleo.objects.all()
    serializer_class = EmpleoSerializer


class PostulacionList(generics.ListCreateAPIView):
    queryset = Postulacion.objects.all()
    serializer_class = PostulacionSerializer

class VerPostulacionList(generics.ListCreateAPIView):
    queryset = Postulacion.objects.all()
    serializer_class = VerPostulacionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id_postulante', 'id_empleo']


class PostulacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Postulacion.objects.all()
    serializer_class = PostulacionSerializer



class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

