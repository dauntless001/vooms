from django.db import models

class GenderChoice(models.TextChoices):
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'

class AdmissionTypeChoice(models.TextChoices):
    A_LEVEL = 'alevel', 'A Level'
    UTME = 'utme', 'UTME'
    DE = 'de', 'Direct Entry'
