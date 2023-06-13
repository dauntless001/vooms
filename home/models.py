from django.db import models
from django.contrib.auth.models import AbstractUser
from voomsdb.utils.models import PersonalModel, NameTimeBasedModel
from voomsdb.utils.choices import AdmissionTypeChoice
from voomsdb.utils.media import MediaHelper
from voomsdb.utils.strings import generate_ref_no
# Create your models here.

class User(AbstractUser):
    pass





class Student(PersonalModel):
    matric_number = models.CharField(max_length=40)
    admission_type = models.CharField(max_length=40, 
                                      choices=AdmissionTypeChoice.choices, 
                                      default=AdmissionTypeChoice.UTME)
    programme = models.ForeignKey('programme.Programme', 
                                  on_delete=models.SET_NULL, null=True, blank=True)
    year_of_admission = models.IntegerField()
    slug = models.SlugField(default=generate_ref_no, null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    
    def image_url(self):
        return self.image.url



class Document(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ForeignKey('home.Student', on_delete=models.CASCADE)
    document = models.FileField(upload_to=MediaHelper.get_document_upload_path)
    slug = models.SlugField(default=generate_ref_no, null=True, blank=True)

    def __str__(self):
        return f'{self.profile} {self.name}'
