from django.db import models
from django.contrib.auth.models import AbstractUser



class BaseModel(models.Model):
    class Meta:
        abstract=True



class User(AbstractUser,BaseModel):
    test=models.CharField(max_length=255, verbose_name='test')
