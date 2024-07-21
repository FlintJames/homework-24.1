from django.contrib import admin
from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'description', 'preview']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'description', 'video_link', 'preview', 'course']