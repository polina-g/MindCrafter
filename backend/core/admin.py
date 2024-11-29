from django.contrib import admin

from core.models import TaskStatus, TaskCategory, TaskNote, Subtask

admin.site.register(TaskStatus)
admin.site.register(TaskCategory)
admin.site.register(TaskNote)
admin.site.register(Subtask)
