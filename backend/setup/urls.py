from django.contrib import admin
from django.urls import path,include
from peghgo.views import PersonalInformationViewSet, ContactInformationViewSet, AcademicViewSet, ExperienceViewSet, CandidateViewSet
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API",
      default_version='v1',
      description="Documentação da API Escola",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('dados_pessoais',PersonalInformationViewSet,basename='Estudantes')
router.register('contatos',ContactInformationViewSet,basename='Contato')
router.register('formacoes',AcademicViewSet,basename='Formacoes')
router.register('experiencias',ExperienceViewSet,basename='Experiencias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
   #  path('estudantes/<int:pk>/matriculas/',ListaMatriculaEstudante.as_view()),
   #  path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]