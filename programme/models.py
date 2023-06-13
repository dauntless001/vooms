from django.db import models
from voomsdb.utils.models import TimeBasedModel
# Create your models here.
class Programme(TimeBasedModel):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
