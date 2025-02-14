from django.shortcuts import render
from . import models

def main(request):
    return render(request, 'base.html')

def active_student_list(request):
    students = models.ActiveStudent.objects.all()
    return render(request, 'active_student.html', {'students': students})

def background_view(request):
    images = models.FonImage.objects.all()  
    return render(request, 'background.html', {'images': images})
