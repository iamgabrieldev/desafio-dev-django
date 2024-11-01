from peghgo.models import PersonalInformation, ContactInformation, ProfessionalExperience, AcademicBackground, Resume, Skill, Candidate
from peghgo.serialiazers import  CandidateSerializer, ProfessionalExperienceSerializer, ContactInformationSerializer, PersonalInformationSerializer, AcademicBackgroundSerializer, ResumeSerializer
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from peghgo.throttles import ResumeAnonRateThrottle, CandidateThrottle

# Create your views here.

# class PersonalInformationViewSet(viewsets.ModelViewSet):
#     queryset = PersonalInformation.objects.all().order_by("id")
#     serializer_class = PersonalInformation
#     filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
#     ordering_fields = ['name', 'social_security_number']
#     search_fields = ['name','social_security_number']

# class ContactInformationViewSett(viewsets.ModelViewSet):
#     """
#     Descrição da ViewSet:
#     - Endpoint para CRUD de contato.

#     Métodos HTTP Permitidos:
#     - GET, POST, PUT, PATCH, DELETE
#     """
#     queryset = ContactInformation.objects.all().order_by("id")
#     serializer_class = ContactInformation

# class ExperienceViewSet(viewsets.ModelViewSet):
#     """
#     Descrição da ViewSet:
#     - Endpoint para CRUD de experiências profissionais.

#     Métodos HTTP Permitidos:
#     - GET, POST

#     Throttle Classes:
#     - ExperienceAnonRateThrottle: limite de taxa para usuários anônimos.
#     - UserRateThrottle: limite de taxa para usuários autenticados.
#     """
#     queryset = ProfessionalExperience.objects.all().order_by("id")
#     serializer_class = ProfessionalExperience
#     http_method_names = ["get", "post"]

class PersonalInformationViewSet(viewsets.ModelViewSet):
    queryset = PersonalInformation.objects.all().order_by("id")
    serializer_class = PersonalInformationSerializer

class ContactInformationViewSet(viewsets.ModelViewSet):
    queryset = ContactInformation.objects.all().order_by("id")
    serializer_class = ContactInformationSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalExperience.objects.all().order_by("id")
    serializer_class = ProfessionalExperienceSerializer
    
class AcademicViewSet(viewsets.ModelViewSet):
    queryset = AcademicBackground.objects.all()
    def get_queryset(self):
        return super().get_queryset().order_by("university")
    serializer_class = AcademicBackgroundSerializer
    
class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['personal_information__name']
    throttle_classes = [CandidateThrottle,UserRateThrottle]
    
class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['personal_information']
    search_fields = ['personal_information__name','personal_information__social_security_number']
    throttle_classes = [ResumeAnonRateThrottle,UserRateThrottle]