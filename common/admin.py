from django.contrib import admin
from . import models

@admin.register(models.Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'image')
    search_fields = ('full_name', 'position')
    list_filter = ('full_name', 'position')


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'likes')
    search_fields = ('title', 'description')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'text')

    def has_add_permission(self, request):
        return False  # Qo'shish (Create) bloklanadi

    def has_change_permission(self, request, obj=None):
        return False  # O'zgartirish (Update) bloklanadi

    def has_delete_permission(self, request, obj=None):
        return False  # O'chirish (Delete) bloklanadi

