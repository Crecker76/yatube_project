from django.db import models


class CreatedModel(models.Model):
    """Абстрактная модель добавляет дату создания."""
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )

    class Meta:
        # Абстрактная модель
        abstract = True