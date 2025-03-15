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


class Teacher(BaseModel):
    ''' Teachers working at the school '''
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='teacher_image')

    def __str__(self):
        return f"{self.full_name} | {self.position}"


class News(BaseModel):
    ''' School in news '''
    title = models.CharField(max_length=550)
    description = models.TextField()
    image = models.ImageField(upload_to='news_image', null=True, blank=True)
    views = models.ManyToManyField(User, related_name='view_count', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked_news', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"



class ActiveStudent(BaseModel):
    ''' Active students dict '''
    full_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='active_student_img')

    def __str__(self):
        return f"{self.full_name}"


class FaceOfSchool(BaseModel):
    ''' Face of school  '''
    CHOICES = [
        ("TEACHER", "O'qtuvchi"),
        ("STUDENT", "O'quvchi")
    ]
    full_name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='face_image')
    description = models.CharField(max_length=550)
    choices = models.CharField(choices=CHOICES, max_length=20, default='TEACHER')

    def __str__(self):
        return f"{self.full_name}"

class FonImage(BaseModel):
    image = models.ImageField(upload_to='fon_images')
