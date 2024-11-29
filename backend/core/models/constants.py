from django.db.models.enums import TextChoices

class PriorityOption(TextChoices):
    HIGHEST = ("highest",)
    HIGH = ("high",)
    LOW = ("low",)
    LOWEST = ("lowest", )
