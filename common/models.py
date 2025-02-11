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


class Notifications(BaseModel):
    ''' Notification model for test and new '''
    message = models.CharField(max_length=550)
    link = models.CharField(max_length=255, null=True, blank=True)
    is_sent = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='notification_user', null=True, blank=True)

    def __str__(self):
        return f"{self.message}"


class Test(BaseModel):
    ''' Test model for school subjects '''
    CLASS_CHOICES = [
        ('5-CLASS', '5-sinf'),
        ('6-CLASS', '6-sinf'),
        ('7-CLASS', '7-sinf'),
        ('8-CLASS', '8-sinf'),
        ('9-CLASS', '9-sinf'),
        ('10-CLASS', '10-sinf'),
        ('11-CLASS', '11-sinf')
    ]
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='test_objects')
    title = models.CharField(max_length=550)
    start_dat = models.DateTimeField(default=None, null=True, blank=True)
    end_data = models.DateTimeField(default=None, null=True, blank=True)
    class_choices = models.CharField(choices=CLASS_CHOICES, max_length=20, default='5-CLASS')

    def __str__(self):
        return f"{self.title} | {self.class_choices}"


class Questions(BaseModel):
    ''' Questions model for test '''
    TRUE_ANSWER_CHOICES = [
        ('A', 'a'),
        ('B', 'b'),
        ('C', 'c'),
        ('D', 'd')
    ]
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='question_test')
    true_answer = models.CharField(choices=TRUE_ANSWER_CHOICES, max_length=5, default='A')
    variant_a = models.CharField(max_length=255)
    variant_b = models.CharField(max_length=255)
    variant_c = models.CharField(max_length=255)
    variant_d = models.CharField(max_length=255)

    def __str__(self):
        return f" {self.test} | {self.true_answer}"


class ActiveStudent(BaseModel):
    ''' Active students dict '''
    full_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=20)
    description = models.CharField(max_length=550)
    image = models.ImageField(upload_to='active_student_img')

    def __str__(self):
        return f"{self.full_name}"
