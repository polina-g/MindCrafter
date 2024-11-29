from core.models.mixins import TimeStampMixin
from django.db.models import TextField
from core.models.fields import StringField
from core.models.constants import PriorityOption
from django.db.models import IntegerField, BooleanField

class Subtask(TimeStampMixin):
    description = TextField(blank=False, null=False)
    priority = StringField(null=True, blank=True, choices=PriorityOption.choices)
    order = IntegerField(null=False, blank=False)
    is_complete = BooleanField(null=False, blank=False, default=False)


    class Meta:
        db_table = "subtask"
        verbose_name = "Subtask"
        verbose_name_plural = "Subtasks"
