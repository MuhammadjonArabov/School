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

class Comment(BaseModel):
    ''' Comment model for news '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    new = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comment_new')
    text = models.TextField()

    def __str__(self):
        return f"{self.user} | {self.new}"




