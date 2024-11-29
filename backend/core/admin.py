from django.contrib import admin

from core.models import TaskStatus, TaskCategory, TaskNote, Subtask, Task

admin.site.register(TaskStatus)
admin.site.register(TaskCategory)
admin.site.register(TaskNote)
admin.site.register(Subtask)
admin.site.register(Task)
