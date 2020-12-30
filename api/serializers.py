from rest_framework.serializers import ModelSerializer
from api.models import Endereco, Curso, Profissional, Perfil


class EnderecoSerializer(ModelSerializer):

    class Meta:
        model = Endereco
        fields = '__all__'


class CursoSerializer(ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'


class ProfissionalSerializer(ModelSerializer):

    class Meta:
        model = Profissional
        fields = '__all__'


class PerfilSerializer(ModelSerializer):

    class Meta:
        model = Perfil
        fields = '__all__'
