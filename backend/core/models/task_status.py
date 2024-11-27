from django.db import models

from core.models.fields import StringField
from core.models.mixins import TimeStampMixin
from colorfield.fields import ColorField


class TaskStatus(TimeStampMixin):
    title = StringField(blank=True)
    bg_color = ColorField(blank=False, null=False, default='#FFFFFF')
    txt_color = ColorField(blank=True, null=False, default='#000000')

    class Meta:
        db_table = "task_status"
        verbose_name = "Task Status"
        verbose_name_plural = "Task Statuses"
