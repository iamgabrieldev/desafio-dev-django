from rest_framework import serializers
from peghgo.models import AcademicBackground, PersonalInformation, ProfessionalExperience, ContactInformation, Candidate, Skill, Resume
from peghgo.validators import social_security_number_invalid, name_invalid, phone_number__invalid, date_invalid

class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = '__all__'

    def validate(self,dados):
        if social_security_number_invalid(dados['social_security_number']):
            raise serializers.ValidationError({'social_security_number':'O CPF deve ter um valor válido'})
        if name_invalid(dados['name']):
            raise serializers.ValidationError({'name':'O name só pode ter letras'})
        if phone_number__invalid(dados['celular']):
            raise serializers.ValidationError({'celular':'O celular precisa seguir o modelo: 86 99999-9999 (respeitando traços e espaços)'})
        return dados
    

class AcademicBackgroundSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    university = serializers.CharField()
    course = serializers.CharField()
    period = serializers.CharField()
    
    class Meta:
        model = AcademicBackground
        fields = 'start_date','end_date','university','course','period'
        
    def validate(self,dados):
        if date_invalid(dados['start_date'],dados['end_date']):
            raise serializers.ValidationError({'end_date':'A data de término não pode ser anterior à data de início'})

class ProfessionalExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalExperience
        fields = '__all__'
    
    def validate(self,dados):
        if date_invalid(dados['start_date'],dados['end_date']):
            raise serializers.ValidationError({'end_date':'A data de término não pode ser anterior à data de início'})

class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'
    def get_phone_number(self):
        return self.phone_number

class CandidateSerializer(serializers.ModelSerializer):
    personal_information = serializers.ReadOnlyField(source = 'personal_information.name')
    class Meta:
        model = Candidate
        fields = ['personal_information']
        
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id','student_name','name']
        
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id','personal_information','contact_information','experiences','academic_background','skills']