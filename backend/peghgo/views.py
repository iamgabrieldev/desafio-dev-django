from peghgo.models import PersonalInformation, ContactInformation, ProfessionalExperience, AcademicBackground
from peghgo.serialiazers import  
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from peghgo.throttles import ResumeAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnl

# Create your views here.

class PersonalInformationViewSet(viewsets.ModelViewSet):
    queryset = DadosPessoais.objects.all().order_by("id")
    serializer_class = DadosPessoaisSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']

class ContactInformationViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de contato.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = ContactInformation.objects.all().order_by("id")
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

class AcademicSerializaer(viewsets.ModelViewSet):
    queryset = FormacaoAcademica.objects.all()  # Adicione essa linha
    def get_queryset(self):
        return super().get_queryset().order_by("universidade")
    serializer_class = AcademicSerializer
    