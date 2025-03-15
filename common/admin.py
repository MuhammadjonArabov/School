from django.contrib import admin
from . import models


@admin.register(models.Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 'image')
    search_fields = ('full_name', 'position')
    list_filter = ('full_name', 'position')


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'description')

@admin.register(models.ActiveStudent)
class ActiveStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'class_name', 'image')
    list_filter = ('class_name',)
    search_fields = ('full_name', 'class_name', 'description')

@admin.register(models.FaceOfSchool)
class FaceOfSchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'image', 'choices')
    list_filter = ('choices',)

@admin.register(models.FonImage)
class FonImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
