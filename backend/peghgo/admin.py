from django.contrib import admin
from peghgo.models import PersonalInformation, ContactInformation, AcademicBackground, ProfessionalExperience, Resume, Skill

class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ('id','name','social_security_number')
    list_display_links = ('id','name')
    search_fields = ('name',)
    
admin.site.register(PersonalInformation, PersonalDataAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number','postal_code','address')
    search_fields = ('postal_code','phone_number')

admin.site.register(ContactInformation, ContactAdmin)

class AcademicAdmin(admin.ModelAdmin):
    list_display = ('id','university','course','period')
    list_display_links = ('id',)

admin.site.register(AcademicBackground, AcademicAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id','company','job_title','start_date','end_date')
    list_display_links = ('id','company',)
    search_fields = ('company',)

admin.site.register(ProfessionalExperience,ExperienceAdmin)

class ResumeAdmin(admin.ModelAdmin):
    def experience(self, obj):
        return ', '.join([exp.company for exp in obj.experiences.all()])

    def academic_background(self, obj):
        return ', '.join([back.university for back in obj.academic_background.all()])

    def skills(self, obj):
        return ', '.join([skill.name for skill in obj.skills.all()])

    list_display = ('id','personal_information','contact_information', 'skills', 'experience', 'academic_background')
    list_display_links = ('id','personal_information', 'contact_information')
    search_fields = ('personal_information__name',)

admin.site.register(Resume,ResumeAdmin)

class SkillAdmin(admin.ModelAdmin):
    def student_name(self, obj):
        return obj.student_name.name

    list_display = ('id','student_name')
    list_display_links = ('id','student_name')
    search_fields = ('student_name__name',)

admin.site.register(Skill,SkillAdmin)