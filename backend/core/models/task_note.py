from core.models.fields import StringField
from core.models.mixins import TimeStampMixin


class TaskNote(TimeStampMixin):
    description = StringField(blank=False, null=False)

    class Meta:
        db_table = "task_note"
        verbose_name = "Task Note"
        verbose_name_plural = "Task Notes"
