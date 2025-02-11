from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subjects(BaseModel):
    ''' Subjects names in school '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class ClassName(BaseModel):
    ''' class name in school '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Teacher(BaseModel):
    ''' teachers working at the school '''
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} | {self.position}"

