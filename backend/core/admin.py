from django.contrib import admin
from django.utils.html import format_html

from core.models import TaskStatus, TaskCategory, TaskNote, Subtask, Task

admin.site.register(TaskCategory)
admin.site.register(TaskNote)
admin.site.register(Subtask)
admin.site.register(Task)


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ("get_full_color",)

    @admin.display(description="color")
    def get_full_color(self, obj):
        return format_html(
            '<div style="width: 100px; height: 30px; background-color: {}; color: {}; text-align: center; line-height: 30px; border: 1px solid #ccc;">{}</div>',
            obj.bg_color,
            obj.txt_color,
            obj.title
        )
