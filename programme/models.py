import auto_prefetch
from django.db import models
from voomsdb.utils.models import TimeBasedModel
# Create your models here.
class College(TimeBasedModel):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Programme(TimeBasedModel):
    name = models.CharField(max_length=255)
    college = auto_prefetch.ForeignKey("programme.College", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
