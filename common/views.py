from django.shortcuts import render
from . import models

def main(request):
    return render(request, 'base.html')

def active_student_list(request):
    students = models.ActiveStudent.objects.all()
    context = {'students': students}
    return render(request, 'active_student.html', context)