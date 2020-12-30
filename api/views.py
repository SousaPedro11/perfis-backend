from rest_framework.viewsets import ModelViewSet
from api.serializers import EnderecoSerializer, CursoSerializer, ProfissionalSerializer, PerfilSerializer
from api.models import Endereco, Curso, Profissional, Perfil


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.order_by('pk')
    serializer_class = EnderecoSerializer


class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.order_by('pk')
    serializer_class = CursoSerializer


class ProfissionalViewSet(ModelViewSet):
    queryset = Profissional.objects.order_by('pk')
    serializer_class = ProfissionalSerializer


class PerfilViewSet(ModelViewSet):
    queryset = Perfil.objects.order_by('pk')
    serializer_class = PerfilSerializer
