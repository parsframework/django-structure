from django.db import models



class BaseModel(models.Model):
    class Meta:
        abstract=True


class Site(BaseModel):

    test=models.CharField(max_length=255, verbose_name='test')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='created_at')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='updated_at')

    def get_absolute_url(self):
        return ''
