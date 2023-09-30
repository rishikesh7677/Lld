from django.db import models

class BaseModel(models.Model):
    crerated = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField()
    active  = models.BooleanField()
    class Meta:
        abstract=True 
        