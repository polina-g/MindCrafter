from django.contrib import admin

from core.models import TaskStatus, TaskCategory, TaskNote

admin.site.register(TaskStatus)
admin.site.register(TaskCategory)
admin.site.register(TaskNote)
