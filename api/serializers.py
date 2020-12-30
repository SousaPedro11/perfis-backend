from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Endereco, Curso, PessoaCurso, Profissional, Perfil


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class ProfissionalSerializer(ModelSerializer):
    formacao = serializers.SerializerMethodField()
    residencia = serializers.SerializerMethodField()

    class Meta:
        extra_kwargs = {
            'curso': {
                'write_only': True
            },
            'endereco': {
                'write_only': True
            }
        }
        model = Profissional
        fields = '__all__'

    def get_formacao(self, instance):
        retorno = ''
        if instance.curso:
            retorno = instance.curso.__str__()
        return retorno

    def get_residencia(self, instance):
        return instance.endereco.__str__()


class PessoaCursoSerializer(ModelSerializer):
    curso = CursoSerializer(read_only=True)
    profissional = ProfissionalSerializer(read_only=True)

    class Meta:
        model = PessoaCurso
        fields = [
            'curso',
            'profissional'
        ]


class PerfilSerializer(ModelSerializer):
    profissional = ProfissionalSerializer()

    class Meta:
        # extra_kwargs = {'profissional': {'write_only': True}, }
        model = Perfil
        fields = '__all__'

    # def get_pessoa(self, instance):
    #     serializer = ProfissionalSerializer(instance.profissional)
    #     return serializer.data

    def create(self, validated_data):
        profissional_data = validated_data.pop('profissional')
        profissional = Profissional.objects.create(**profissional_data)
        perfil = Perfil.objects.create(**validated_data, profissional=profissional)
        return perfil
