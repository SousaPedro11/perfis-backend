from rest_framework.viewsets import ModelViewSet
from api.serializers import EnderecoSerializer, CursoSerializer, PessoaCursoSerializer, ProfissionalSerializer, PerfilSerializer
from api.models import Endereco, Curso, PessoaCurso, Profissional, Perfil


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.order_by('pk')
    serializer_class = EnderecoSerializer


class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.order_by('pk')
    serializer_class = CursoSerializer


class PessoaCursoViewSet(ModelViewSet):
    queryset = PessoaCurso.objects.order_by('pk')
    serializer_class = PessoaCursoSerializer


class ProfissionalViewSet(ModelViewSet):
    queryset = Profissional.objects.order_by('pk')
    serializer_class = ProfissionalSerializer


class PerfilViewSet(ModelViewSet):
    queryset = Perfil.objects.order_by('pk')
    serializer_class = PerfilSerializer
