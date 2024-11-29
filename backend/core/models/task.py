from core.models.mixins import TimeStampMixin
from django.db.models import TextField, ForeignKey, PROTECT, DateTimeField
from core.models.fields import StringField
from core.models.constants import PriorityOption
from core.models.task_status import TaskStatus
from core.models.task_category import TaskCategory
from core.models.task_note import TaskNote
from core.models.subtask import Subtask
from django.db.models.indexes import Index

class Task(TimeStampMixin):
    status = ForeignKey(TaskStatus, blank=False, null=False, on_delete=PROTECT,)
    category = ForeignKey(TaskCategory, blank=True, null=True, on_delete=PROTECT,)
    notes = ForeignKey(TaskNote, blank=True, null=True, on_delete=PROTECT,)
    subtask = ForeignKey(Subtask, blank=True, null=True, on_delete=PROTECT,)

    description = TextField(blank=False, null=False)
    priority = StringField(null=True, blank=True, choices=PriorityOption.choices)
    due_date_time = DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        indexes = [
            Index(fields=["status"]),
            Index(fields=["category"])
        ]
