from django.db import models
from django.core.validators import RegexValidator

class PersonalInformation(models.Model):
    """
    Model representing an individual's personal information.
    """
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, max_length=100)
    date_of_birth = models.DateField()
    social_security_number = models.CharField(max_length=11, unique=True)
    mobile_phone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\d{2} \d{5}-\d{4}$', message='Please enter a valid mobile phone number.')])

    def __str__(self):
        return self.name


class ContactInformation(models.Model):
    """
    Model representing contact information.
    """
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=8)

    def __str__(self):
        return self.phone_number


class ProfessionalExperience(models.Model):
    """
    Model representing professional experience.
    """
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.company


class AcademicBackground(models.Model):
    """
    Model representing academic background.
    """
    university = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.university


class Skill(models.Model):
    """
    Model representing skills.
    """
    name = models.CharField(max_length=100)
    student_name = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name.name


class Resume(models.Model):
    """
    Model representing a resume.
    """
    personal_information = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    contact_information = models.OneToOneField(ContactInformation, on_delete=models.CASCADE)
    experiences = models.ManyToManyField(ProfessionalExperience)
    academic_background = models.ManyToManyField(AcademicBackground)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.personal_information.name


class Candidate(models.Model):
    """
    Model representing a candidate.
    """
    personal_information = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE, related_name='candidate')
    contact_information = models.OneToOneField(ContactInformation, on_delete=models.CASCADE, related_name='candidate')
    experiences = models.ManyToManyField(ProfessionalExperience, related_name='candidates')
    academic_background = models.ManyToManyField(AcademicBackground, related_name='candidates')
    skills = models.ManyToManyField(Skill, related_name='candidates')

    def __str__(self):
        return self.personal_information.name