from django.contrib import admin

from demo101.tasks.models import Task


# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done')
    list_filter = ('done',)

