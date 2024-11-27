from django.db.models import CharField


class StringField(CharField):
    """CharField with max length of 4096"""

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 4096
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs