from django.db import models
from voomsdb.utils.media import MediaHelper
from voomsdb.utils.choices import GenderChoice

class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class NameTimeBasedModel(TimeBasedModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class PersonalModel(NameTimeBasedModel):
    image = models.ImageField(upload_to=MediaHelper.get_image_upload_path, null=True, blank=True)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    mobile_no = models.IntegerField()
    gender = models.CharField(max_length=30, choices=GenderChoice.choices, default=GenderChoice.FEMALE)
    
    class Meta:
        abstract = True
