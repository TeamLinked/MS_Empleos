from rest_framework import serializers
from .models import Usuario, Empleo, Postulacion, Categoria

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmpleoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleo
        fields = '__all__'

class PostulacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Postulacion
        fields = '__all__'


class VerPostulacionSerializer(serializers.ModelSerializer):
    id_empleo = EmpleoSerializer(read_only=True)
    #id_postulante = UsuarioSerializer( read_only=True)
    class Meta:
        model = Postulacion
        fields = ('id', 'id_postulante', 'id_empleo', 'fechaAplicacion')



class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = '__all__'

#('id','id_postulante', 'id_empleo','fechaAplicacion')