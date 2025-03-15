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

def teachers_list(request):
    teachers = models.Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def faces_of_school(request):
    faces = models.FaceOfSchool.objects.all()
    return render(request, 'faces_of_school.html', {'faces': faces})