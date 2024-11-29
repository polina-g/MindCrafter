from django.contrib import admin

from core.models import TaskStatus, TaskCategory

admin.site.register(TaskStatus)
admin.site.register(TaskCategory)
