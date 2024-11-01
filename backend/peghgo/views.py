from peghgo.models import DadosPessoais, Contato, Experiencia, FormacaoAcademica, Habilidade, Resume, Candidatos
from peghgo import DadosPessoaisSerializer, ContatoSerializer, ExperienciaSerializer, FormacaoAcademicaSerializer, HabilidadeSerializer, ResumeSerializer 
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from peghgo.throttles import ResumeAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnl

# Create your views here.

class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = DadosPessoais.objects.all().order_by("id")
    serializer_class = DadosPessoaisSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']

class ContactViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de contato.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Contato.objects.all().order_by("id")
    serializer_class = ContatoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ExperienceViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de experiências profissionais.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """
    queryset = Experiencia.objects.all().order_by("id")
    serializer_class = ExperienciaSerializer
    http_method_names = ["get", "post"]

class AcadenucViewSet(viewsets.ModelViewSet):
    queryset = FormacaoAcademica.objects.all()  # Adicione essa linha
    def get_queryset(self):
        return super().get_queryset().order_by("universidade")
    serializer_class = FormacaoAcademicaSerializer
    
class Skills(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Habilidade.order_by("nome")
        return queryset
    serializer_class = HabilidadeSerializer
