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


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'new', 'text')
    list_filter = ('user',)

    def has_add_permission(self, request):
        return False  # Qo'shish (Create) bloklanadi

    def has_change_permission(self, request, obj=None):
        return False  # O'zgartirish (Update) bloklanadi

    def has_delete_permission(self, request, obj=None):
        return False  # O'chirish (Delete) bloklanadi


@admin.register(models.Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'is_sent', 'user')
    list_filter = ('is_sent', 'message')


@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'subjects', 'class_choices')
    list_filter = ('class_choices', 'subjects')

@admin.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'true_answer', 'question_text')
    list_filter = ('test',)

@admin.register(models.ActiveStudent)
class ActiveStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'class_name', 'image')
    list_filter = ('class_name',)
    search_fields = ('full_name', 'class_name', 'description')

@admin.register(models.FaceOfSchool)
class FaceOfSchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'image', 'choices')
    list_filter = ('choices',)

