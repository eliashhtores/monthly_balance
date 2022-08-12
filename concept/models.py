from django.db import models
from model_utils.models import TimeStampedModel


class Concept(TimeStampedModel):
    EXTERNAL = 'EX'
    INTERNAL = 'IN'
    CONCEPT_CHOICES = (
        (EXTERNAL, 'External'),
        (INTERNAL, 'Internal'),
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=CONCEPT_CHOICES)

    class Meta:
        unique_together = ('name', 'type')

    def __str__(self):
        return self.name
