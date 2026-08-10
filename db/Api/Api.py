from django.db import models



class BaseModel(models.Model):
    class Meta:
        abstract=True



class Api(BaseModel):
    test=models.CharField(max_length=255, verbose_name='test')
