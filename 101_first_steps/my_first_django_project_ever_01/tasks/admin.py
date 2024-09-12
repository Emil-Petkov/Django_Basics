from django.contrib import admin

from my_first_django_project_ever_01.tasks.models import Task


# Register your models here.

# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "done",)
    list_filter = ("title", "done",)
